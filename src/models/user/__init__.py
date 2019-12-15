from src import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String (200))
    mobile = db.Column(db.String, unique=True)
    email = db.Column(db.String (200), index = True, unique=True)
    # address = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(1200))
    tokens = db.relationship("Token", backref="user", lazy=True)
    order = db.relationship("Order", backref="user", lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def check_user(self):
        return User.query.filter_by(email=self.email).first()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def get_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "mobile": self.mobile,
            "email": self.email
        }

class Token(db.Model):
    __tablename__="tokens"
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, unique= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

db.create_all()