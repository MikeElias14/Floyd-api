import yfinance as yf
from models.holding_model import unused_info, unused_history, unused_index_info


def get_info(tickers, index=False):
    info = []
    for ticker in tickers:
        yf_ticker = yf.Ticker(ticker)
        try:
            ticker_info = yf_ticker.info

            # Get rid of things I don't currently use
            if index:
                remove_info = unused_index_info
            else:
                remove_info = unused_info

            for field in remove_info:
                if field in ticker_info:
                    ticker_info.pop(field)

            info.append(dict(ticker=ticker, info=ticker_info))

        except:
            ticker_info = "Bug"  # TODO: Fix this, https://github.com/ranaroussi/yfinance/issues/208
            info.append(dict(ticker=ticker, info=ticker_info))

    return info


def get_div(tickers):
    divideds = []
    for ticker in tickers:
        yf_ticker = yf.Ticker(ticker)
        try:
            ticker_div = yf_ticker.dividends.to_dict()

            dict_div = []
            for obj in ticker_div:
                dict_div.append({obj.strftime('%Y/%m/%d'): ticker_div[obj]})

            divideds.append(dict(ticker=ticker, history=dict_div))

        except:
            ticker_div = [dict(bug=1)]  # TODO: Fix this, https://github.com/ranaroussi/yfinance/issues/208
            divideds.append(dict(ticker=ticker, history=ticker_div))

    return divideds


def get_events(tickers):
    events = []
    for ticker in tickers:
        yf_ticker = yf.Ticker(ticker)
        try:
            ticker_events = yf_ticker.calendar.to_dict()

        except:
            ticker_events = "Bug"  # TODO: Fix this, https://github.com/ranaroussi/yfinance/issues/208

        events.append(dict(ticker=ticker, events=ticker_events))

    return events


def get_history(tickers, time, interval):
    tickers_history = []
    for ticker in tickers:
        yf_ticker = yf.Ticker(ticker)

        try:
            history = yf_ticker.history(period=time, interval=interval, prepost=False, actions=False).to_dict()

            for field in unused_history:
                if field in history:
                    history.pop(field)

            ticker_history = []
            for obj in history['Close']:
                ticker_history.append({obj.strftime('%Y/%m/%d'): history['Close'][obj]})
            tickers_history.append(dict(ticker=ticker, history=ticker_history))

        except:
            history = "Bug"  # TODO: Fix this, https://github.com/ranaroussi/yfinance/issues/208
            tickers_history.append(dict(ticker=ticker, history=history))

    return tickers_history
