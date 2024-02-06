
from . import db
from . import app
from flask_login import UserMixin
from datetime import datetime

from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100),unique=True)
    name = db.Column(db.String(1000),unique=True)
    workouts = db.relationship('Workout2', backref='author', lazy=True)
    
class Workout2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_body_area = db.Column(db.Text, nullable=False)
    number_of_sets = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
with app.app_context():
    db.create_all()  