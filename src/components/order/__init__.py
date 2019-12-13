from src.models.user import User
from src.models.user import Token
from src.models.service import Service
from src.models.order import Order
from src.models.location import Location
from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required

from src import app, db

order_blueprint = Blueprint('orders', __name__)

@order_blueprint.route('/schedule-service', methods=['POST', 'GET'])
@login_required
def schedule():
    if request.method == 'POST':
        data = request.get_json()['order']
        check_serv = Service.query.filter_by(service_name = data['servicetype']).first()
        print(check_serv,'service here')
        addr = Location.query.filter_by(location_pickup = data['address']).first()
        if not addr:
            address = Location(location_pickup = data['address'])
            db.session.add(address)
            db.session.commit()
        order_item = Order(user_id=current_user.id, service_id=check_serv.id, dateandtime=data['dateandtime'], location_id=addr.id)
        db.session.add(order_item)
        db.session.commit()
        return jsonify({'success':'success'})

        

