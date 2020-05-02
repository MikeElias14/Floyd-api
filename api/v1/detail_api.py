import json
from flask import Blueprint, jsonify, request
import controllers.detail_controller as controller

detail_bp = Blueprint('detail', __name__, url_prefix='/detail')

# Get One or More or All detail
@detail_bp.route('', methods=["GET"])
def get_detail():
    ticker = request.args.get('ticker') or None

    if ticker is not None:
        result = controller.get_detail(ticker)
        code = 200
    else:
        result = 'error'
        code = 400

    return jsonify(result), code
