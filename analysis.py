import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import yfinance as yf
from urllib.request import urlopen
from datetime import datetime, timedelta, date
import plotly.express as px
import plotly.graph_objects as go

#------------------------------------------------------------------------------------------------------#
#                                           ANNUAL DIFFERENCE                                          #
#------------------------------------------------------------------------------------------------------#

# Loading datasets
bitcoin = pd.read_csv('Bitcoin.csv')
ethereum = pd.read_csv('Ethereum.csv')

# Fuction used to obtain yearly dates
def YearIncrement(timeframe):
    start_date = "2017-11-08"
    next_year = int(start_date[:4]) + timeframe
    start_date= str(next_year) + start_date[4:]
    next_date = start_date
    return next_date

# Getting annual closing price difference
def ClosingPriceDifference(table):
    start = []
    end = []
    for num in range(6):
        start.append(YearIncrement(num))
        end.append(YearIncrement(num+1))
    annual_performance = pd.DataFrame({'Start Date': start, 'End Date': end})
    start_date = list(annual_performance['Start Date'])
    end_date = list(annual_performance['End Date'])
    difference = []
    for num in range(len(annual_performance)):
        value = (table[table['Date'] == end_date[num]]['Close'].max()) - (table[table['Date'] == start_date[num]]['Close'].max())
        difference.append(value)
    difference

    annual_performance['Closing Price Difference'] = difference
    return annual_performance

# Target dataframes
annual_performance_bitcoin = ClosingPriceDifference(bitcoin).dropna()
annual_performance_ethereum = ClosingPriceDifference(ethereum).dropna()
# compiled_annual_performance = annual_performance_ethereum.merge(annual_performance_ethereum, how = 'inner', on = 'Start Date')


def ReturnTable(num):
    if num == 1:
        return annual_performance_bitcoin
    elif num == 2:
        return annual_performance_ethereum
    # elif num == 3:
    #    return compiled_annual_performance



#--------------------------------------------------------------------------------------------------------------------------------#
#                                                 2018 CRASH                                                                     #
#--------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------- PLOTTING FUNCTION-------------------------------------------------------
def PlottingFunction(x,y1,y2,name1,name2, color1, color2,title,xtitle,ytitle):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x= x, y= y1, name= name1, line=dict(color= color1, width=2)))
    fig.add_trace(go.Scatter(x= x, y= y2, name= name2, line=dict(color= color2, width=2)))
    fig.update_layout(title = title,
            xaxis_title=xtitle,
            yaxis_title= ytitle)
    st.plotly_chart(fig, use_container_width= True)
