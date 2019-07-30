from flask_app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    index = db.Column(db.Integer)
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='profile1.png')
    password = db.Column(db.String(60), nullable=False)
    papers = db.relationship('Paper', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"


class Paper(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    contentId = db.Column(db.BIGINT, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String)
    text = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    journal = db.Column(db.Text)
    userID = db.Column(db.BIGINT, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.title}', '{self.year}')"
