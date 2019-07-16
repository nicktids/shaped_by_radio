from app import db
from sqlalchemy import BINARY, Column, Date, Float, Integer, MetaData,Unicode,String,Numeric,DECIMAL,TypeDecorator,BigInteger,ForeignKey

class Station(db.Model):
    id = Column(Integer, primary_key=True)
    station = Column(String(64), index=True, unique=True)
    country = Column(String(64), index=True)

    def __repr__(self):
        return '<station {}>'.format(self.station)

class Broadcaster(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    show_name = Column(String(100))
    broadcast_pid = Column(String(20))
    station_id = Column(Integer, ForeignKey('station.id'))

class Episode(db.Model):
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    ep_pid = Column(String(20))
    duration = Column(Integer)
    title = Column(String(100))
    broadcast_id = Column(Integer, ForeignKey('broadcaster.id'))

    def __repr__(self):
        return f'<Episode {self.ep_pid} - {self.title}>'    

class Artist(db.Model):
    id = Column(Integer, primary_key=True)
    

class tracks(db.Model):
    id = Column(Integer, primary_key=True)
    artist = Column(String(100))
    track_title = Column(String(100))
    position = 
    

    