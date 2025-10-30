from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<User {self.username} {self.points}>'
