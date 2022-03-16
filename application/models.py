from application import db

class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)