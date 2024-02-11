#This code was written with the help of my mentor, useful to get stock prices. Current is set for: 'AAPL','MSFT','TWLO','EURRUB=X'

# %%
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf # https://pypi.org/project/yfinance/
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

# %%
###########
# sidebar #
###########
option = st.sidebar.selectbox('Select Stock', ('AAPL','MSFT','TWLO','EURRUB=X'))

import datetime

today = datetime.date.today()
before = today - datetime.timedelta(days=30)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')




# %%
##############
# Stock data #
##############

# Download data
df = yf.download(option,start=start_date,end=end_date, progress=False)
# Bollinger Bands
indicator_bb = BollingerBands(df['Close'])
bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Close','bb_h','bb_l']]

# Moving Average Convergence Divergence
macd = MACD(df['Close']).macd()

# Resistence Strength Indicator
rsi = RSIIndicator(df['Close']).rsi()




# %%
###################
# Set up main app #
###################

# Plot the prices and the bolinger bands
st.write('Stock Bollinger Bands')
st.bar_chart(bb)

progress_bar = st.progress(0)

# Plot MACD
st.write('Stock Moving Average Convergence Divergence (MACD)')
st.bar_chart(macd)

# Plot RSI
st.write('Stock RSI ')
st.area_chart(rsi)

# Data of recent days
st.write('Recent data ')
st.dataframe(df.tail(10))
# %%
