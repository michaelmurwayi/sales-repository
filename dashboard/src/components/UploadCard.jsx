// src/components/UploadCard.jsx
import { Button, Card, CardContent } from "@mui/material";
import { useDispatch } from "react-redux";
import { fetchForecast } from "../features/forecast/forecastSlice";

export default function UploadCard() {
  const dispatch = useDispatch();

  const handleUpload = (e) => {
    const file = e.target.files[0];
    if (file) dispatch(fetchForecast(file));
  };

  return (
    <Card>
      <CardContent>
        <input type="file" onChange={handleUpload} />
        <Button variant="contained" component="span">
          Upload CSV
        </Button>
      </CardContent>
    </Card>
  );
}
