# from requests.exceptions import HTTPError
from flask import Blueprint, render_template, request, jsonify
from src.models.user import User
from src.models.place import Place
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

from src import app, db

place_blueprint = Blueprint('places', __name__)

@place_blueprint.route('/servicecheck', methods=['POST'])
def check():
    if request.method == 'POST':
        data = request.get_json()['input']
        district = data['district']
        check_service = Place.query.filter_by(District = district).first()
        if check_service:
            return jsonify({'success' : district})
        if not check_service:
            return jsonify({'false' : 'false'})
        
