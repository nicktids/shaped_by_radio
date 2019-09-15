import pandas as pd
from app import app, db
from app.models import Station, Broadcast

from dynaconf import settings

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


from app.shape_scraping import get_show_details

db.create_all()

def add_station(station, country,key_db):
    newstation = Station(station=station, country=country,key=key_db)
    db.session.add(newstation)
    db.session.commit()
    db.session.close

# add_station("Radio1", "UK")

def add_broadcast(pid,short_name):
    bro = get_show_details(pid)

    ky = db.session.query(Station.id).filter(Station.key==bro['station_id_key']).first()

    bro['station_id'] = ky[0]
    bro['shortname'] = short_name
    del bro['station_id_key']

    newBroadcast = Broadcast(**bro)
    db.session.add(newBroadcast)
    db.session.commit()
    db.session.close

    print(f'{bro}')
