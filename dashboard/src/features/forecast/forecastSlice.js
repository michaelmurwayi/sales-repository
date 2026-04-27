// src/features/forecast/forecastSlice.js
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { uploadCSV } from "./forecastAPI";

export const fetchForecast = createAsyncThunk(
  "forecast/fetchForecast",
  async (file) => {
    const data = await uploadCSV(file);
    return data;
  },
);

const forecastSlice = createSlice({
  name: "forecast",
  initialState: {
    data: null,
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchForecast.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchForecast.fulfilled, (state, action) => {
        state.loading = false;
        state.data = action.payload;
      })
      .addCase(fetchForecast.rejected, (state) => {
        state.loading = false;
        state.error = "Failed to load data";
      });
  },
});

export default forecastSlice.reducer;
