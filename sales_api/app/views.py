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

        model = SalesForecaster()
        result = model.run_full_pipeline(df)

        return Response(result)