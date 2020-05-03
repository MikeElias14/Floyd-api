import yfinance as yf


def get_info(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.info


def get_div(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.dividends.to_json()
