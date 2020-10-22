from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import config

# Define db then connect later
db = SQLAlchemy()

def create_app():
    # create and configure the app
    _app = Flask(__name__, instance_relative_config=True)
    CORS(_app)

    _app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI
    )

    # Connect to DB
    db.init_app(_app)

    # Create Routes
    # Holdings
    from api.v1.holding_api import holdings_bp
    _app.register_blueprint(holdings_bp)

    # Users
    from api.v1.holding_api import users_bp
    _app.register_blueprint(users_bp)


    return _app


app = create_app()
app.run(debug=True)
