from src import db
from src.models.user import User
from src.models.place import Place
from src.models.service import Service
from src.models.location import Location

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    dateandtime = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    status = db.Column(db.String, default="Scheduled")
    
    def render(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "service_id": self.service_id,
            "dateandtime": self.dateandtime,
            "location_id": self.location_id,
            "status": self.status
        }

db.create_all()
