from flask import Blueprint, jsonify, request
import controllers.users_controller as controller

users_bp = Blueprint('users', __name__, url_prefix='/users')


# *** CREATE *** #

@users_bp.route('', methods=["POST"])
def create_user():
    name = request.args.get('name') or None

    if name is not None:
        code, result = controller.create_user(name)
    else:
        result = "Name not given"
        code = 400

    return result, code


@users_bp.route('holdings', methods=["POST"])
def add_user_holding():
    user = request.args.get('user_id') or None
    tickers = request.args.get('tickers') or None

    if user is not None and tickers is not None:
        code, result = controller.add_user_holdings(user, tickers)
    else:
        result = "Name not given"
        code = 400

    return result, code


# *** READ *** #

# Get Users info
@users_bp.route('', methods=["GET"])
def get_user_by_name():
    name = request.args.get('name') or None

    if name is not None:
        result = controller.get_user_by_name(name)
        code = 200
    else:
        result = 'No user given'
        code = 400

    if result is None:
        result = 'User not found'
        code = 404

    return jsonify(result), code


# Get Users Holdings info
@users_bp.route('holdings', methods=["GET"])
def get_user_holdings_by_id():
    user_id = request.args.get('user_id') or None

    if user_id is not None:
        result = controller.get_user_holdings(user_id)
        code = 200
    else:
        result = 'No User Specified'
        code = 400

    return jsonify(result), code
