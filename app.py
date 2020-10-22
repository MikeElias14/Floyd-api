from flask import Flask
from flask_cors import CORS
from extensions import db
import config


def create_app():
    # create and configure the app
    _app = Flask(__name__, instance_relative_config=True)
    CORS(_app)

    _app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI
    )

    register_extentions(_app)
    register_blueprints(_app)

    return _app


def register_blueprints(_app):
    # Holdings
    from api.v1.holding_api import holdings_bp
    _app.register_blueprint(holdings_bp)

    # Users
    from api.v1.users_api import users_bp
    _app.register_blueprint(users_bp)


def register_extentions(_app):
    db.init_app(_app)


app = create_app()
app.run(debug=True)
