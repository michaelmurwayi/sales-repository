// src/pages/Dashboard.jsx
import { useSelector } from "react-redux";
import { Grid, Typography } from "@mui/material";

import UploadCard from "../components/UploadCard";
import MetricsCard from "../components/MetricsCard";
import ChartView from "../components/ChartView";
import ForecastTable from "../components/ForecastTable";

export default function Dashboard() {
  const { data } = useSelector((state) => state.forecast);

  if (!data) {
    return (
      <div>
        <UploadCard />
      </div>
    );
  }

  return (
    <div>
      <Typography variant="h4">Sales Forecast Dashboard</Typography>

      <UploadCard />

      <Grid container spacing={2} marginTop={2}>
        <Grid item xs={6}>
          <MetricsCard
            title="Linear Regression"
            metrics={data.models.linear_regression.metrics}
          />
        </Grid>

        <Grid item xs={6}>
          <MetricsCard
            title="Random Forest"
            metrics={data.models.random_forest.metrics}
          />
        </Grid>
      </Grid>

      <Typography variant="h6" marginTop={3}>
        Actual vs Predicted (Best Model: {data.best_model})
      </Typography>

      <ChartView data={data.models[data.best_model]} />

      <Typography variant="h6" marginTop={3}>
        Forecast (Next 7 Days)
      </Typography>

      <ForecastTable data={data.forecast_next_7_days} />
    </div>
  );
}
