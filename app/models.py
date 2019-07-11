from app import db

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(64), index=True, unique=True)
    country = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<station {}>'.format(self.station)

class Broadcaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)