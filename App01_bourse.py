import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price app
         
Shown are the stock closing price and volume of Google
""")

#Define stock
tickerSymbol = "AAPL"

#Get data
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2004-1-1',end='2022-9-2')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)