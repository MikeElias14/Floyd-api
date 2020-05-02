from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    _app = Flask(__name__, instance_relative_config=True)

    # Create Routes
    # Detail
    from api.v1.detail_api import detail_bp
    _app.register_blueprint(detail_bp)

    return _app


app = create_app()
app.run(debug=True)
