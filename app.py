import streamlit as st
import pandas as pd
import joblib

# Load the trained XGBoost model
model = joblib.load("xgboost_volatility.pkl")

# Page title and description
st.title("📈 Crypto Volatility Predictor")
st.markdown("Enter crypto indicators to predict **7-day rolling volatility**.")

# ------------------ User Input Section ------------------ #
open_ = st.number_input("Open", min_value=0.0, value=0.5)
high = st.number_input("High", min_value=0.0, value=0.6)
low = st.number_input("Low", min_value=0.0, value=0.4)
close = st.number_input("Close", min_value=0.0, value=0.5)
volume = st.number_input("Volume", min_value=0.0, value=0.3)
market_cap = st.number_input("Market Cap", min_value=0.0, value=0.7)
ret = st.number_input("Return", min_value=-1.0, max_value=1.0, value=0.01)
liquidity = st.number_input("Liquidity Ratio", min_value=0.0, value=0.02)
ma_7 = st.number_input("MA_7", min_value=0.0, value=0.5)
ma_14 = st.number_input("MA_14", min_value=0.0, value=0.5)
price_range = st.number_input("Price Range", min_value=0.0, value=0.03)

# Create DataFrame from inputs
input_df = pd.DataFrame([{
    'Open': open_,
    'High': high,
    'Low': low,
    'Close': close,
    'Volume': volume,
    'Market Cap': market_cap,
    'Return': ret,
    'Liquidity_Ratio': liquidity,
    'MA_7': ma_7,
    'MA_14': ma_14,
    'Price_Range': price_range
}])

# ------------------ Prediction Section ------------------ #
if st.button("Predict Volatility"):
    prediction = model.predict(input_df)
    st.success(f"📉 Predicted 7-day Volatility: **{prediction[0]:.6f}**")
