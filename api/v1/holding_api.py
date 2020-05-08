from flask import Blueprint, jsonify, request
import controllers.holding_controller as controller

detail_bp = Blueprint('detail', __name__, url_prefix='/holding')


# Get tickers info
@detail_bp.route('info', methods=["GET"])
def get_info():
    tickers = request.args.get('tickers') or None
    index = request.args.get('index') or False

    if index == 'true':
        index = True

    if index == 'false':
        index = False

    if tickers is not None:
        tickers = tickers.split(',')
        result = controller.get_info(tickers, index=index)
        code = 200
    else:
        result = 'No Ticker'
        code = 400

    return jsonify(result), code


# Get ticker dividend history
@detail_bp.route('div', methods=["GET"])
def get_div():
    tickers = request.args.get('tickers') or None

    if tickers is not None:
        tickers = tickers.split(',')
        result = controller.get_div(tickers)
        code = 200
    else:
        result = 'No Ticker'
        code = 400

    return jsonify(result), code


# Get ticker dividend history
@detail_bp.route('events', methods=["GET"])
def get_events():
    tickers = request.args.get('tickers') or None

    if tickers is not None:
        tickers = tickers.split(',')
        result = controller.get_events(tickers)
        code = 200
    else:
        result = 'No Ticker'
        code = 400

    return jsonify(result), code


# Get ticker price history
@detail_bp.route('history', methods=["GET"])
def get_history():
    tickers = request.args.get('tickers') or None
    time = request.args.get('time') or None
    interval = request.args.get('interval') or None

    if tickers is not None and time is not None and interval is not None:
        tickers = tickers.split(',')
        result = controller.get_history(tickers, time, interval)
        code = 200
    else:
        result = 'No Ticker or no time'
        code = 400

    return jsonify(result), code
