# Cryptocurrency Volatility Prediction
This project forecasts 7-day rolling volatility of cryptocurrencies using historical OHLCV data and machine learning (XGBoost Regressor). It helps traders identify risk periods and optimize strategies.

## 📁 Project Highlights

- 📊 **EDA**: Trend analysis, volatility behavior, correlation heatmaps  
- ⚙️ **Features**: Returns, ATR, Bollinger Bands, Liquidity Ratio  
- 🤖 **Model**: XGBoost Regressor with engineered features  
- 📈 **Performance**:
  - MAE ≈ 0.020998 
  - RMSE ≈ 0.056805  
  - R² ≈ 0.2182

## 🧰 Tech Stack

- Python, pandas, scikit-learn, XGBoost  
- matplotlib, seaborn  
- joblib (model saving)  
- Optional: Streamlit for deployment  

## 🗂️ Files & Folders
📂 data/ → Cleaned dataset
📂 models/ → Trained model (.pkl)
📂 docs/ → HLD, LLD, EDA report
📂 visuals/ → EDA graphs
📂 app/ → Streamlit interface (optional)

## 🚀 How to Use

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app (optional)
streamlit run app/streamlit_app.py


## 📎 Deliverables
  - Trained ML model
  - Visual EDA report
  - Full documentation (HLD, LLD, Pipeline)
  - GitHub-friendly structure
