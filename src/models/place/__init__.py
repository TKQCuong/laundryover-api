from src import db

class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    District = db.Column(db.String, nullable=False)
db.create_all()