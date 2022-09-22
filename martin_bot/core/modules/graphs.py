import yfinance as yf
import plotly.graph_objects as go
from plotly.offline import iplot
from plotly.subplots import make_subplots
from finta import TA
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import interact
from itertools import cycle

class StockFeatures:
    
    def __init__(self, df):
        self.base = df
        self.indicators = {}
        

    def add_sma(self,window = 30):
       self.indicators[f'SMA-{window}'] = {
            "indicator_type" : "single",
            "chart_type": ""
            
       }
       TA.SMA(self.base, window).to_list()

    def plot(self):
        trace_array = []
        indicies = self.base.index
        trace_array.append(
            go.Candlestick(x = indicies,
                             open = self.base['Open'],
                             high = self.base['High'],
                             low = self.base['Low'],
                             close = self.base['Close'], showlegend=False,
                             name = 'candlestick',
                             yaxis = "y2",
                             decreasing = {"line": {"color": "#7F7F7F"}},
                             increasing= {"line": {"color": "#17BECF"}}
                             ))
        colour_sequence = cycle(["#7F7F7F" for x in range(5)] + ["#17BECF" for x in range(5)])
        trace_array.append(go.Bar(x = self.base.index, y = self.base['Volume'], showlegend=False,yaxis = "y", type = "bar", marker = {"color": [next(colour_sequence)for i in range(len(self.base['Volume']))]}))
        layout = {
        "yaxis": {
            "domain": [0, 0.5], 
            "showticklabels": False
        }, 
        "legend": {
            "x": 0.3, 
            "y": 0.9, 
            "yanchor": "bottom", 
            "orientation": "h"
        }, 
        "margin": {
            "b": 40, 
            "l": 40, 
            "r": 40, 
            "t": 40
        }, 
        "yaxis2": {"domain": [0.5, 0.95]}, 
        "plot_bgcolor": "rgb(250, 250, 250)"
        }
        fig = Figure(data=trace_array, layout=layout)
        fig.update(layout_xaxis_rangeslider_visible=False)

        for key, value in self.indicators.items():
             fig.add_trace(go.Scatter(x = self.single_channel_indicators.index,
                          y = self.single_channel_indicators[col],
                          name = "candlestick"),
               row = 1, col = 1)
        # fig.update_layout(plot_bgcolor = "rgb(250, 250, 250)")

        return fig        

#sf = StockFeatures(yf.download(tickers='EURUSD=X', period='1y', interval='5d'))
