from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class WeatherSnapshot(db.Model):
    """
    Represent a snapshot of a weather stats for a specific time
    and place.

    Used to cache API calls results.
    """
    __tablename__ = 'weather_snapshots'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer())
    place = db.Column(db.String())
    date = db.Column(db.DateTime())

    def __str__(self):
        return '<WeatherSnapshot id:{id}>'.format(id=self.id)