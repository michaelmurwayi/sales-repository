// src/components/ChartView.jsx
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
} from "recharts";

export default function ChartView({ data }) {
  if (!data) return null;

  const chartData = data.actual.map((a, i) => ({
    index: i,
    actual: a,
    predicted: data.predicted[i],
  }));

  return (
    <LineChart width={700} height={300} data={chartData}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="index" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="actual" stroke="#8884d8" />
      <Line type="monotone" dataKey="predicted" stroke="#82ca9d" />
    </LineChart>
  );
}
