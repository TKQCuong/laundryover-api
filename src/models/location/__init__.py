from src import db


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    location_pickup = db.Column(db.String(200), nullable=False)
    order = db.relationship('Order', backref="location", lazy=True)
    
db.create_all()