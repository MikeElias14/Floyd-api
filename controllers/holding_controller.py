import json
import yfinance as yf
from models.holding_model import unused_info, unused_history


def get_info(ticker):
    ticker = yf.Ticker(ticker)
    info = ticker.info

    # Get rid of things I don't currently use
    for field in unused_info:
        if field in info:
            info.pop(field)

    return info


def get_div(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.dividends.to_json()


def get_history(ticker):
    ticker = yf.Ticker(ticker)
    history = ticker.history(period='10y', interval='1d', prepost=False, actions=False).to_dict()

    for field in unused_history:
        if field in history:
            history.pop(field)

    res_history = []
    for obj in history['Close']:
        res_history.append({obj.strftime('%Y/%m/%d'): history['Close'][obj]})

    return res_history
