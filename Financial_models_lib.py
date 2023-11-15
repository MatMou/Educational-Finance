
#core 
import pandas as pd
import numpy as np

#plots
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# data
import yfinance as yf

#stats
import statsmodels.api as sm


models = {
    'HAR': {
        'params' : ['lags']
    }, 
    'GARCH' :{
        'params' : ['omega', 'alpha', 'beta', ]
    }
}


# Initial functions 

def fetch_data(ticker, start_date, end_date, frequency):
    return yf.download(ticker, start=start_date, end=end_date, interval=frequency)










#################################
#
# Volatility models
#
##################################


# HAR
def realized_volatility(high, low):
    rv = np.log(high/low)**2/(4*np.log(2))
    return rv

def estimate_har_model(realized_vol, lags):
    
    df = pd.DataFrame(index=realized_vol.index,
                     columns=['RV'])
    df['RV'] = realized_vol
    df['Constant'] = [1 for i in range(len(df['RV']))]

    for lag in lags:
        df['RV_L'+str(lag)] = df['RV'].shift(lag)

    df = df.dropna()

    model = sm.OLS(df['RV'], df[df.columns[1:]]).fit()
    print(model.summary())
    
    res = model.fittedvalues
    return model, res


# GARCH
def compute_conditional_volatility(returns, omega, alpha, beta):
    n = len(returns)
    volatility = np.zeros(n)
    volatility_squared = np.zeros(n)
    
    # Initialize volatility_squared
    volatility_squared[0] = np.var(returns)

    for t in range(1, n):
        volatility_squared[t] = omega + alpha * (returns[t - 1] ** 2) + beta * volatility_squared[t - 1]

    # Compute the conditional volatility
    volatility = np.sqrt(volatility_squared)
    
    return volatility




# 
# Plotting functions 
#
#

def plot_har_realized_volalility(high, low, lags):
    realized_vol = realized_volatility(high, low)
    res, har_res = estimate_har_model(realized_vol, lags)

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    
    fig.add_trace(go.Scatter(x=high.index,
                             y=realized_vol,
                             mode='lines',
                             name='Realized Vol',
                             line_color='grey'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(x=high.index[np.max(lags):],
                             y=har_res, mode='lines',
                             name='HAR Model',
                             line_color='darkgreen'),
                  row=2, col=1)

    fig.update_layout(title=f'Realized Volatility and HAR Model with Lags {lags}', xaxis_title='Day', yaxis_title='Returns')
    fig.update_layout(xaxis2=dict(title='Day'), yaxis2=dict(title='Realized Volatility'))
    fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    margin=dict(l=50,r=50,b=100,t=100,pad=4
    ))
    return res, fig



def plot_garch(omega, alpha, beta, returns):
    conditional_volatility = compute_conditional_volatility(returns, omega, alpha, beta)

    # Create traces for financial returns and conditional volatility
    financial_returns_trace = go.Scatter(
        x=returns.index, 
        y=returns, 
        mode='lines', 
        name='Financial Returns',
        line_color='grey'
    )
    conditional_volatility_trace = go.Scatter(
        x=returns.index, 
        y=conditional_volatility, 
        mode='lines', 
        name='Conditional Volatility',
        line_color = 'darkgreen'
    )

    # Define the layout
    layout = go.Layout(
        title='GARCH Model - Financial Returns and Conditional Volatility',
        xaxis_title='Time',
        yaxis_title='Volatility',
        margin=dict(l=50, r=50, b=100, t=100, pad=4)
    )

    # Create the figure and add traces
    fig = go.Figure(data=[financial_returns_trace, conditional_volatility_trace], layout=layout)
    fig.update_layout(
        autosize=False,
        width=800,
        height=600,
        margin=dict(l=50,r=50,b=100,t=100,pad=4)
    )

    # Show the figure
    return fig


























