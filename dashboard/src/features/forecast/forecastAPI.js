// src/features/forecast/forecastAPI.js
import axios from "axios";

const API_URL = "http://localhost:8000/api/forecast/";

export const uploadCSV = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(API_URL, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return res.data;
};
