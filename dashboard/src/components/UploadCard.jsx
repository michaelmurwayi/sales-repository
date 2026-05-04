import React, { useState } from "react";
import {
  Button,
  Card,
  CardContent,
  Typography,
  CircularProgress,
} from "@mui/material";
import { useDispatch, useSelector } from "react-redux";
import { fetchForecast } from "../features/forecast/forecastSlice";

export default function UploadCard() {
  const dispatch = useDispatch();

  const { loading } = useSelector((state) => state.forecast);

  const [fileName, setFileName] = useState("");

  const handleUpload = (e) => {
    const file = e.target.files[0];
    console.log("FILE SELECTED:", file); // 🔥 MUST SHOW

    if (file) {
      setFileName(file.name);
      dispatch(fetchForecast(file));
    }
  };

  return (
    <Card sx={{ padding: 2, marginBottom: 2 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Upload Sales CSV
        </Typography>

        <input
          type="file"
          accept=".csv"
          onChange={handleUpload}
          style={{ marginBottom: 10 }}
        />

        {fileName && (
          <Typography variant="body2" color="text.secondary">
            Selected file: {fileName}
          </Typography>
        )}

        {loading && (
          <div style={{ marginTop: 10 }}>
            <CircularProgress size={24} />
            <Typography variant="body2">Processing...</Typography>
          </div>
        )}

        <Button variant="contained" component="label" sx={{ marginTop: 2 }}>
          Choose File
          <input type="file" hidden onChange={handleUpload} />
        </Button>
      </CardContent>
    </Card>
  );
}
