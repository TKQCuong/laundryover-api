from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
## import Models
from src.models.user import User
from src.models.user import Token
from src.models.order import Order
## import Blueprint
# from src.components.user import user_blueprint 
# app.register_blueprint(user_blueprint, url_prefix='/userpd')


## set up Login_manager
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "userpd.login

from src.components.user import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/")

from src.components.place import place_blueprint
app.register_blueprint(place_blueprint, url_prefix="/")

from src.components.order import order_blueprint
app.register_blueprint(order_blueprint, url_prefix="/")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(id)


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Token ', '', 1)
        token = Token.query.filter_by(uuid=api_key).first()
        if token:
            return token.user
    return None
