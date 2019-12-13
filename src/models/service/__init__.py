from src import db

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(200), nullable=False)
    order = db.relationship('Order', backref="service", lazy=True)

db.create_all()