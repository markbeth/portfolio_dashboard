import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf

tickers = ["AAPL", "MSFT"]
end_date = pd.Timestamp.now()
start_date = end_date - pd.Timedelta(days=30)

data = pd.DataFrame()
for ticker in tickers:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    data[ticker] = stock_data['Close']

data = data.reset_index().rename(columns={'index': 'Date'})

st.title("Portfolio Tracking Dashboard")

st.subheader("Portfolio Timeseries Data")
st.write(data)


# Pie Chart Portfolio Distribution (with latest closing values)
st.subheader("Portfolio Distribution")
latest_values = data.iloc[-1, 1:]
fig = px.pie(
    values=latest_values.values,
    names=latest_values.index,
    title="Portfolio Distribution (Latest Prices)"
)
st.plotly_chart(fig)

# Line Chart for a Selected Asset
st.subheader("Stock price dynamics")
selected_asset = st.selectbox("Select Asset", options=tickers)
filtered_data = data[['Date', selected_asset]].set_index('Date')
st.line_chart(filtered_data, width=700)
