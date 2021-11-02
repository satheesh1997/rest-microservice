from app.main import db


class Uptime(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    started   = db.Column(db.Boolean, default=True)
    timestamp = db.Column(db.DateTime)
