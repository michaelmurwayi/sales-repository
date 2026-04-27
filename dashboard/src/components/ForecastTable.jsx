// src/components/ForecastTable.jsx
import {
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
} from "@mui/material";

export default function ForecastTable({ data }) {
  if (!data) return null;

  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>Date</TableCell>
          <TableCell>Prediction</TableCell>
        </TableRow>
      </TableHead>

      <TableBody>
        {data.map((row, i) => (
          <TableRow key={i}>
            <TableCell>{row.date}</TableCell>
            <TableCell>{row.prediction}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
