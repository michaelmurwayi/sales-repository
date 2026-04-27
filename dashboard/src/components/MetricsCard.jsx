// src/components/MetricsCard.jsx
import { Card, CardContent, Typography, Grid } from "@mui/material";

export default function MetricsCard({ title, metrics }) {
  if (!metrics) return null;

  return (
    <Card>
      <CardContent>
        <Typography variant="h6">{title}</Typography>

        <Grid container spacing={2}>
          <Grid item xs={4}>
            MAE: {metrics.mae}
          </Grid>
          <Grid item xs={4}>
            RMSE: {metrics.rmse}
          </Grid>
          <Grid item xs={4}>
            R²: {metrics.r2}
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
}
