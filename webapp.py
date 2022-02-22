"""
Analysis of Top Cryptocurrencies

"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import yfinance as yf
from urllib.request import urlopen
from live import LivePrices

###########Header

st.set_page_config(page_title = "Cryptocurrency Analysis", page_icon = 
":moneybag:", layout="wide")
st.markdown("##")

####Image

###########Sidebar
sBox = st.sidebar.selectbox("Menu", ["Home","Overview","Live", "Analysis", "Recommendation", "Conclusion", "The Team"])
#st.sidebar.selectbox("Topics", ["Popularity", "Trends","Stability", "Growth", "Risk"])

#############Pages

def OverviewPage(sBox):
    if sBox == "Home":
        st.markdown("<h1 style='text-align: center; color: black;'> Cryptocurrency Performance Index </h1>", unsafe_allow_html=True)
        st.write()
        st.write()
        #st.title("Cryptocurrency Performance Index")
        imagemain = Image.open(r"C:\\Users\\HP\\OneDrive\\Desktop\\Moringa\\webapp\\images\\main.jpg")
        st.image(imagemain, caption="Cryptocurrency")
        st.markdown("##")
    elif sBox == "Overview":
        st.markdown("<h2 style='text-align: center; color: black;'> Cryptocurrency Overview </h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2,6,1])

        with col1:
            st.write("")

        with col2:
            imageOverview = Image.open(r"C:\\Users\\HP\\OneDrive\\Desktop\\Moringa\\webapp\\images\\Cryptocurrency-Wallets.jpg")
            st.image(imageOverview, caption="Cryptocurrency", width= 500)

        with col3:
            st.write("")
        
        st.write("\n\n\n\n\n")
        st.write(""" Cryptocurrency is a digital currency, also referred to as a digital asset. These digital
        assets operate in a network known as the blockchain.Blockchain is a shared, immutable ledger
        that facilitates the process of recording transactions and tracking assets in a business network.
        (point of failure) The inception of the cryptocurrency world started in the year 2009; after the
        2007 global economic crisis when financial institutions sank and assets plummeted. A man
        named   Satoshi   Nakamoto(never   proven   if   he/she   exists)   introduced   the   bitcoin
        whitepaper(Investopedia, 2022). The idea of bitcoin and the blockchain was to oppose the
        control governments have through the various banking systems and return some freedoms to the
        users of the banking system. It is also an alternative to store wealth which is not subject to factors such as inflation or
        recessions. Cryptocurrency is bought through markets or decentralized exchanges although over the years some of these exchanges
        have been centralized.""")
        st.write( """
        A cryptocurrency exchange (crypto   exchange) is a platform that promotes the trade of cryptocurrencies using digital money,
        fiat money or other assets. These exchanges are the intermediaries   between   parties   and   make   money   from   transaction
        fees   and   commissions. Cryptocurrency bought via these markets can be stored digitally with a hot wallet(online wallet)
        or a cold wallet(physical wallet - in the form of a USB). It is important to note that once a wallet is lost coins can never be 
        recovered. Over the years, many digital assets have been created to serve different purposes. The downside with crypto-assets is
        that the exchanges on which they are traded on are prone to mass hacking which results in loss of millions of dollars across all
        investor accounts; although there are forms in which you can store your coins and not be as susceptible to hacking. The return on
        investment from crypto assets is much higher than returns from bank investments. """)
        #st.subheader("Cryptocurrency Overview")
    
    elif sBox == "Live" :
        LivePrices()

    elif sBox == "Analysis":
        analysisRad = st.sidebar.radio("Topics", ["Trends", "Popularity", "Stability", "Growth", "Risk"]) 
        if analysisRad == "Trends":
            st.subheader("Trends")
        elif analysisRad == "Popularity":
            st.subheader("Popularity")
        elif analysisRad == "Stability":
            st.subheader("Stability")
        elif analysisRad == "Growth":
            st.subheader("Growth")
        elif analysisRad == "Risk":
            st.subheader("Risk")
    elif sBox == "Recommendation":
        st.subheader("Recommendation")
    elif sBox == "Conclusion":
        st.subheader("Conclusion")
    elif sBox == "The Team":
        st.subheader("Team Members")

OverviewPage(sBox)


    
    