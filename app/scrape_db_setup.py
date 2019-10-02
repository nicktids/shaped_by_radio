import pandas as pd
from app import app, db
from app.models import Station, Broadcast, Show



from dynaconf import settings

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


import app.shape_scraping as ss

db.create_all()

def add_station(station, country,key_db):
    newstation = Station(station=station, country=country,key=key_db)
    db.session.add(newstation)
    db.session.commit()
    db.session.close()


# add_station("Radio1", "UK")

def add_broadcast(pid,short_name):
    """To add a new broadcast show to the broadcast table.
    
    Arguments:
        pid {[str]} -- [description]
        short_name {[type]} -- [description]
    """
    bro = ss.get_show_details(pid)

    ky = db.session.query(Station.id).filter(Station.key==bro['station_id_key']).first()

    bro['station_id'] = ky[0]
    bro['shortname'] = short_name
    del bro['station_id_key']

    newBroadcast = Broadcast(**bro)
    db.session.add(newBroadcast)
    db.session.commit()
    db.session.close()

    # print(f'{bro}')

def showsToGrab():
    bro = Broadcast.query.all()
    shows_list = []
    for b in bro:
        cal = ss.get_show_calendar(b.pid)
        
        for yr in cal:
            for mth in cal[yr]:
                shows_list.extend(ss.get_shows_in_mth(b.pid,yr,mth))

    #  ------------------ compare to what is in the db and then grab all the shows no there

    return shows_list

    


def add_show(pid):
    print("test")


def add_track():
    """add track to the db
    """
    print("test")


    