import pandas as pd
from app import app, db
from app.models import Station

from dynaconf import settings

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


db.create_all()

def add_station(station, country):
    newstation = Station(station=station, country=country)
    db.session.add(newstation)
    db.session.commit()

# add_station("Radio1", "UK")
