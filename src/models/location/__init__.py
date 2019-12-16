from src import db


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    location_pickup = db.Column(db.String(200), nullable=False)
    order = db.relationship('Order', backref="location", lazy=True)
    def render(self):
        return {
            "id" : self.id,
            "location_pickup" : self.location_pickup
        }
db.create_all()