import yfinance as yf
from models.holding_model import unused_info


def get_info(ticker):
    ticker = yf.Ticker(ticker)
    info = ticker.info

    # Get rid of things I don't currently use
    for field in unused_info:
        info.pop(field)

    return info


def get_div(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.dividends.to_json()
