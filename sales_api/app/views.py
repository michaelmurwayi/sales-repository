from rest_framework.views import APIView
from rest_framework.response import Response

import pandas as pd

from services.forecast_service import SalesForecaster


class SalesForecastView(APIView):

    def post(self, request):

        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        df = pd.read_csv(file)

        required = ["Sale_Date", "Sales_Amount"]

        for col in required:
            if col not in df.columns:
                return Response({"error": f"Missing column: {col}"}, status=400)

        # =========================
        # INIT FORECASTER
        # =========================
        model = SalesForecaster()

        # =========================
        # TRAIN MODELS
        # =========================
        results = model.train(df)

        """
        Expected structure from train():
        results = {
            "linear_regression": {
                "score": ...,
                "actual": [...],
                "predicted": [...]
            },
            "random_forest": {
                "score": ...,
                "actual": [...],
                "predicted": [...]
            }
        }
        """

        # =========================
        # FORECAST FUTURE
        # =========================
        forecast = model.predict_next(df, days_ahead=7)

        # =========================
        # RESPONSE
        # =========================
        return Response({
            "models": {
                "linear_regression": {
                    "score": results["linear_regression"]["score"],
                    "actual": results["linear_regression"]["actual"],
                    "predicted": results["linear_regression"]["predicted"]
                },
                "random_forest": {
                    "score": results["random_forest"]["score"],
                    "actual": results["random_forest"]["actual"],
                    "predicted": results["random_forest"]["predicted"]
                }
            },
            "forecast_next_7_days": forecast
        })