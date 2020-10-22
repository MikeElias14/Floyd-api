from flask import Blueprint, jsonify, request
import controllers.users_controller as controller

detail_bp = Blueprint('users', __name__, url_prefix='/users')

# *** CREATE *** #

# *** READ *** #

# Get Users info
@detail_bp.route('holdings', methods=["GET"])
def get_user_by_name():
    name = request.args.get('user_name') or None
    if name is not None:
        result = controller.get_user_by_name(name)
        code = 200
    else:
        result = 'User Not found'
        code = 400

    return jsonify(result), code


# Get Users Holdinds info
@detail_bp.route('holdings', methods=["GET"])
def get_user_holdings_by_id():
    user_id = request.args.get('user_id') or None
    if user_id is not None:
        result = controller.get_user_holdings(user_id)
        code = 200
    else:
        result = 'No User Specified'
        code = 400

    return jsonify(result), code
