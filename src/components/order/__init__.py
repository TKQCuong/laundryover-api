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
        # addr = Location.query.filter_by(location_pickup = data['address']).first()
        # if not addr:
        address = Location(user_id = current_user.id, location_pickup = data['address'])
        db.session.add(address)
        db.session.commit()
        order_items = Order(user_id=current_user.id, service_id=check_serv.id, dateandtime=data['dateandtime'], location_id=address.id)
        db.session.add(order_items)
        db.session.commit()
        return jsonify({'success':'success'})

    
@order_blueprint.route('/getData', methods=['GET'])
@login_required
def renderOrder():
    orders = Order.query.filter_by(user_id = current_user.id).all()
    orders = Order.query.order_by(Order.id.desc()).all()
    locations = Location.query.all()
    return jsonify({"order": [order.render() for order in orders],
                    "location": [location.render() for location in locations]})
                
@order_blueprint.route('/cancelOrder/<id>', methods=['PUT'])
@login_required
def cancelOrder(id):
    data = request.get_json()
    cancel_order = data['cancel']
    check_status = Order.query.filter_by(id = id).first()
    if check_status:
        check_status.status = cancel_order
        db.session.commit()
        return jsonify({'success':True})