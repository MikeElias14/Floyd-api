from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime)
    name = db.Column(db.String(128), nullable=False)


class UserHoldings(db.Model):
    __tablename__ = 'user_holdings'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    holding_id = db.Column(db.BigInteger, db.ForeignKey('holdings.id'), nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)


class Holdings(db.Model):
    __tablename__ = 'holdings'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String(128), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=False)


if __name__ == '__main__':
    manager.run()
