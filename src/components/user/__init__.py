# from requests.exceptions import HTTPError
from flask import Blueprint, render_template, request, jsonify
from src.models.user import User
from src.models.user import Token
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
import uuid

from src import app, db

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user(user)

@user_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()['input']
        email = data['email']
        password_hash = data['password']
        user = User.query.filter_by(email = email).first()
        if not user:
            return jsonify({'false' : 'not email'})
        if user.check_password(password_hash):
            token = Token.query.filter_by(user_id=user.id).first()
            if not token:
                token = Token(user_id=user.id,
                                uuid=str(uuid.uuid4().hex))
                db.session.add(token)
                db.session.commit()
            login_user(user)
            print('Successfully log in as', email)
            return jsonify({'email': email, 'username' : user.username, 'mobile' : user.mobile, "token": token.uuid})
        return jsonify({'false' : 'wrong pass'})
    return jsonify({'email' : 'false'})

@user_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = request.get_json()['input']
        username = data['username']
        email = data['email']
        password_hash = data['password']
        mobile = data['mobile']
        # address = data['address']
        check_mobile = User.query.filter_by(mobile=mobile).first()
        if check_mobile:
            return jsonify({'false':'existed mobile'})
        user = User.query.filter_by(email = email).first()
        if user:
            print("You've already have account, please sign in")
        if not user:
            user = User(email=email, username=username, mobile=mobile)
            user.set_password(password_hash)
            db.session.add(user)
            db.session.commit()
            new_token = Token(
                user_id=user.id, uuid=str(uuid.uuid4().hex))
            db.session.add(new_token)
            db.session.commit()
            print("Registered success!", user.email)
            return jsonify({'email':email, 'username': username, 'mobile': mobile, "token": new_token.uuid})
    return jsonify({'false' : 'false'})

@user_blueprint.route('/getinfo', methods=['POST', 'GET'])
def get_user():
    if request.method == 'POST':
        return jsonify({"asdsadasdad":"adadadasd"})
    token = request.headers.get('Authorization').split(' ')[1]
    reaccess_user = Token.query.filter_by(uuid=token).first()
    print('reaccess_user',reaccess_user)
    if reaccess_user:
        return jsonify(reaccess_user.user.get_json())
    return jsonify({ "hello": "world"})

@user_blueprint.route('/dashboard', methods=['PUT'])
@login_required
def edit_user():
        data = request.get_json()['update']
        username = data['username']
        email = current_user.email
        mobile = data['mobile']
        user = User.query.filter_by(email=email).first()
        user.username = username
        user.email = email
        user.mobile = mobile
        user.set_password(data['password'])
        db.session.commit()
        print('update success')
        return jsonify({'username':username, 'email':email, 'mobile':mobile})
    


