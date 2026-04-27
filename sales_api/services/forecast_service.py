import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class SalesForecaster:

    def __init__(self):
        self.lr = LinearRegression()
        self.rf = RandomForestRegressor(n_estimators=100, random_state=42)

    # =========================
    # DATA PREPROCESSING
    # =========================
    def _prepare(self, df):

        df = df.copy()

        df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
        df = df.sort_values("Sale_Date")

        df["Year"] = df["Sale_Date"].dt.year
        df["Month"] = df["Sale_Date"].dt.month
        df["Day"] = df["Sale_Date"].dt.day

        X = df[["Year", "Month", "Day"]]
        y = df["Sales_Amount"]

        return X, y, df

    # =========================
    # METRICS
    # =========================
    def _metrics(self, y_true, y_pred):

        return {
            "mae": float(mean_absolute_error(y_true, y_pred)),
            "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
            "r2": float(r2_score(y_true, y_pred))
        }

    # =========================
    # FORECAST FUTURE
    # =========================
    def _forecast(self, model, df, days_ahead=7):

        last_date = df["Sale_Date"].max()

        future_dates = pd.date_range(
            start=last_date,
            periods=days_ahead + 1,
            freq="D"
        )[1:]

        future_df = pd.DataFrame({"Sale_Date": future_dates})

        future_df["Year"] = future_df["Sale_Date"].dt.year
        future_df["Month"] = future_df["Sale_Date"].dt.month
        future_df["Day"] = future_df["Sale_Date"].dt.day

        X_future = future_df[["Year", "Month", "Day"]]

        preds = model.predict(X_future)

        return [
            {
                "date": str(date),
                "prediction": float(pred)
            }
            for date, pred in zip(future_dates, preds)
        ]

    # =========================
    # FULL PIPELINE
    # =========================
    def run_full_pipeline(self, df):

        X, y, df = self._prepare(df)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )

        # =========================
        # TRAIN MODELS
        # =========================
        self.lr.fit(X_train, y_train)
        lr_pred = self.lr.predict(X_test)

        self.rf.fit(X_train, y_train)
        rf_pred = self.rf.predict(X_test)

        # =========================
        # METRICS
        # =========================
        lr_metrics = self._metrics(y_test, lr_pred)
        rf_metrics = self._metrics(y_test, rf_pred)

        # =========================
        # BEST MODEL SELECTION
        # =========================
        if lr_metrics["rmse"] < rf_metrics["rmse"]:
            best_model_name = "linear_regression"
            best_model = self.lr
        else:
            best_model_name = "random_forest"
            best_model = self.rf

        # =========================
        # FORECAST USING BEST MODEL
        # =========================
        forecast = self._forecast(best_model, df)

        # =========================
        # FINAL RESPONSE
        # =========================
        return {
            "comparison": {
                "linear_regression": lr_metrics,
                "random_forest": rf_metrics
            },
            "best_model": best_model_name,
            "models": {
                "linear_regression": {
                    "metrics": lr_metrics,
                    "actual": y_test.tolist(),
                    "predicted": lr_pred.tolist()
                },
                "random_forest": {
                    "metrics": rf_metrics,
                    "actual": y_test.tolist(),
                    "predicted": rf_pred.tolist()
                }
            },
            "forecast_next_7_days": forecast
        }