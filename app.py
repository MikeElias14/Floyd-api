from flask import Flask
from flask_cors import CORS
import logging


def create_app():
    # create and configure the app
    _app = Flask(__name__, instance_relative_config=True)
    CORS(_app)

    # Create Routes
    # Detail
    from api.v1.holding_api import detail_bp
    _app.register_blueprint(detail_bp)

    return _app


app = create_app()
app.run(debug=True)
