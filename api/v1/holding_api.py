import json
from flask import Blueprint, jsonify, request
import controllers.holding_controller as controller

detail_bp = Blueprint('detail', __name__, url_prefix='/holding')


# Get ticker info
@detail_bp.route('info', methods=["GET"])
def get_info():
    ticker = request.args.get('ticker') or None

    if ticker is not None:
        result = controller.get_info(ticker)
        code = 200
    else:
        result = 'No Ticker'
        code = 400

    return jsonify(result), code


# Get ticker dividend history
@detail_bp.route('div', methods=["GET"])
def get_div():
    ticker = request.args.get('ticker') or None

    if ticker is not None:
        result = controller.get_div(ticker)
        code = 200
    else:
        result = 'No Ticker'
        code = 400

    return jsonify(result), code


# Get ticker price history
@detail_bp.route('history', methods=["GET"])
def get_history():
    ticker = request.args.get('ticker') or None

    if ticker is not None:
        result = controller.get_history(ticker)
        code = 200
    else:
        result = 'No Ticker'
        code = 400

    return jsonify(result), code
