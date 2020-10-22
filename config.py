import os

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_URI = os.environ.get("DB_URI")

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_URI}/floyd"