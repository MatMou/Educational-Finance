
import streamlit as st
import numpy as np
import plotly.graph_objs as go
import Financial_models_lib as fm 
from datetime import datetime


st.set_page_config(page_title="Volatility Models", page_icon=":books:")
st.header('Visualize your first model')

model = st.selectbox('Select your model', fm.models.keys())

with st.sidebar:
    ticker = st.selectbox('Pick your stock', ['MSFT', 'TSLA', '^DJI'])
    start_date = st.date_input('Pick the start of the returns')
    freq = st.selectbox('What frequency?', ['1d', '1wk', '1mo'])
    end_date = datetime.today()

    if model == "HAR":
        lags = st.multiselect('What lags do you want in your model?', [i for i in range(30)])

    elif model == "GARCH":
        omega = st.number_input('Omega', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
        alpha = st.number_input('Alpha', min_value=0.0, max_value=1.0, value=0.1, step=0.01)
        beta = st.number_input('Beta', min_value=0.0, max_value=1.0, value=0.8, step=0.01)
        

    
if st.button("Compute"):
    with st.spinner('Black magic in process'):

        if model == 'HAR':
            prices = fm.fetch_data(ticker, start_date, end_date, freq)
            res, plt = fm.plot_har_realized_volalility(prices['High'], prices['Low'], lags)
            st.plotly_chart(plt)
            st.text(res.summary())

        elif model == 'GARCH': 
            returns = (fm.fetch_data(ticker, start_date, end_date, freq)['Adj Close']).pct_change().dropna()
            plt = fm.plot_garch(omega, alpha, beta, returns)
            st.plotly_chart(plt)
