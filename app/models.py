from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    date_created = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<User {self.username} {self.points} {self.date_created}>'
