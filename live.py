import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import yfinance as yf
from urllib.request import urlopen
from datetime import datetime, timedelta, date
import plotly.express as px
import plotly.graph_objects as go

def LivePrices():
    
    # Titles and subtitles

    st.title("Cryptocurrencies")
    st.header("Prices Dashboard")
    
    # Ticker variable definition

    Bitcoin = 'BTC-USD'
    Etherium = 'ETH-USD'
    Litecoin = 'LTC-USD'
    Dogecoin = 'DOGE-USD'
    Monero = 'XMR-USD'

    # Data access from Yahoo finance

    BTC_Data = yf.Ticker(Bitcoin)
    ETH_Data = yf.Ticker(Etherium)
    LTC_Data = yf.Ticker(Litecoin)
    DOGE_Data = yf.Ticker(Dogecoin)
    XMR_Data = yf.Ticker(Monero)

    # Fetching of historical data 

    BTC_Hist = BTC_Data.history(period="max")
    ETH_Hist = ETH_Data.history(period="max")
    LTC_Hist = LTC_Data.history(period="max")
    DOGE_Hist = DOGE_Data.history(period="max")
    XMR_Hist = XMR_Data.history(period="max")

    # Fetching datasets

        # Setting time limits
    current = datetime.today()
    yesterday = current - timedelta(days = 1)

    BTC = yf.download(Bitcoin, start= yesterday, end = current.strftime("%Y-%m-%d"))
    ETH = yf.download(Etherium, start= yesterday, end = current.strftime("%Y-%m-%d"))
    LTC = yf.download(Litecoin, start= yesterday, end = current.strftime("%Y-%m-%d"))
    DOGE = yf.download(Dogecoin, start= yesterday, end =  current.strftime("%Y-%m-%d"))
    XMR = yf.download(Monero, start= yesterday, end = current.strftime("%Y-%m-%d"))
    BTC_class = yf.download(Bitcoin, start= "2017-11-09", end = "2022-02-22")
    ETH_class = yf.download(Bitcoin, start= "2017-11-09", end = "2022-02-22")

    # Data sourcing
    # BTC_class.to_csv("Bitcoin.csv")
    # ETH_class.to_csv("Ethereum.csv")
    

    # Displaying cryptocurrencies

    # Currency image variables
    BTC_image = 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'
    ETH_image = 'https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'
    LTC_image = 'https://s2.coinmarketcap.com/static/img/coins/64x64/2.png'
    DOGE_image = 'https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'
    XMR_image = 'https://s2.coinmarketcap.com/static/img/coins/64x64/328.png'

    # Display function
    def displayCurrencies(label, image, table, historical_data, color):
        label = label.upper() + " ($)"
        # Displaying currency name
        st.write(label)
        # Currency image
        imageCoin = Image.open(urlopen(image))
        st.image(imageCoin)
        # Displaying Yahoo Finance table
        st.table(table)
        # Line Chart Display
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data.Close, name='Closing Price', line=dict(color=color, width=2)))
        fig.update_layout(title=(label + ' Closing Price'),
                   xaxis_title='Year',
                   yaxis_title='Closing Price')
        st.plotly_chart(fig, use_container_width= True)
       



    # Bitcoin
    displayCurrencies("bitcoin", BTC_image, table = BTC, historical_data = BTC_Hist, color = 'orange')
    # Etherium
    displayCurrencies("etherium", ETH_image, table = ETH, historical_data = ETH_Hist, color = 'purple')
    # Litecoin
    # displayCurrencies("litecoin", LTC_image, table = LTC, historical_data = LTC_Hist, color = 'blue')
    # Dogecoin
    # displayCurrencies("dogecoin", DOGE_image, table = DOGE, historical_data = DOGE_Hist, color = 'green')
    # Monero
    # displayCurrencies("monero", XMR_image, table = XMR, historical_data = XMR_Hist, color = 'red')
  
