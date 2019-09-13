from app import db
from sqlalchemy import BINARY, Column, Date, Float, Integer, MetaData,Unicode,String,Numeric,DECIMAL,TypeDecorator,BigInteger,ForeignKey

class Station(db.Model):
    id = Column(Integer, primary_key=True)
    station = Column(String(64), index=True, unique=True)
    country = Column(String(64), index=True)

    def __repr__(self):
        return '<station {}>'.format(self.station)

class Broadcast(db.Model):
    id = Column(Integer, primary_key=True)
    pid = Column(String(10))
    shortname = Column(String(10))
    presenter = Column(String(100))
    show_name = Column(String(100))
    first_broadcast_date = Column(Date)
    image_pid = Column(String(20)) #could make it a dic later on
    station_id = Column(Integer, ForeignKey('station.id'))

class Show(db.Model):
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    ep_pid = Column(String(20))
    image_pid = Column(String(20))
    duration = Column(Integer)
    title = Column(String(100))
    desc_short = Column(String(200))
    desc_med = Column(String(500))
    desc_long = Column(String(3000))
    broadcast_id = Column(Integer, ForeignKey('broadcast.id'))


    def __repr__(self):
        return f'<Episode {self.ep_pid} - {self.title}>'    

class Artist(db.Model):
    id = Column(Integer, primary_key=True)
    artist_name = Column(String(100))
    musicbrainz_gid = Column(String(100))
    bbc_artist_pid = Column(String(10))
    
    
class track(db.Model):
    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey('artist.id'))
    track_title = Column(String(200))
    bbc_track_pid = Column(String(200))
    

class show_track_position(db.Model):
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('show.id'))
    track_id = Column(Integer, ForeignKey('track.id'))
    show_position = Column(Integer)
    duration = Column(Float())
    show_offset = Column(Float())    

class special_title(db.Model):
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('show.id'))
    track_id = Column(Integer, ForeignKey('track.id'))
    special_title = Column(String(100))

