from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd


class SalesForecaster:

    def __init__(self):
        self.lr = LinearRegression()
        self.rf = RandomForestRegressor(n_estimators=100, random_state=42)

    def _prepare(self, df):

        df = df.copy()
        df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
        df = df.sort_values("Sale_Date")

        df["Year"] = df["Sale_Date"].dt.year
        df["Month"] = df["Sale_Date"].dt.month
        df["Day"] = df["Sale_Date"].dt.day

        features = ["Year", "Month", "Day"]
        X = df[features]
        y = df["Sales_Amount"]

        return X, y, df

    # =========================
    # TRAIN BOTH MODELS
    # =========================
    def train(self, df):

        X, y, df = self._prepare(df)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )

        # Linear Regression
        self.lr.fit(X_train, y_train)
        lr_pred = self.lr.predict(X_test)

        # Random Forest
        self.rf.fit(X_train, y_train)
        rf_pred = self.rf.predict(X_test)

        return {
            "linear_regression": {
                "score": float(self.lr.score(X_test, y_test)),
                "actual": y_test.tolist(),
                "predicted": lr_pred.tolist()
            },
            "random_forest": {
                "score": float(self.rf.score(X_test, y_test)),
                "actual": y_test.tolist(),
                "predicted": rf_pred.tolist()
            }
        }

    # =========================
    # FORECAST FUTURE
    # =========================
    def predict_next(self, df, days_ahead=7):

        df = df.copy()
        df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

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

        lr_pred = self.lr.predict(X_future)
        rf_pred = self.rf.predict(X_future)

        return [
            {
                "date": str(date),
                "linear_regression": float(lr),
                "random_forest": float(rf)
            }
            for date, lr, rf in zip(future_dates, lr_pred, rf_pred)
        ]