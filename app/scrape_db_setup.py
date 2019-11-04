import pandas as pd
from app import app, db
from app.models import Station, Broadcast, Show

from dynaconf import settings

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

import app.shape_scraping as ss

db.create_all()

# pandas example 
# q = scrape_db_setup.db.session.query(scrape_db_setup.Broadcast)
# df = pd.read_sql(q.statement,scrape_db_setup.db.engine)


def add_station(station: str, country: str,key_db):
    """adds a new station
    
    Parameters
    ----------
    station : str
        station name
    country : [type]
        [description]
    key_db : [type]
        [description]
    """
    newstation = Station(station=station, country=country, key=key_db)
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

def grab_all_show_pid(broadcast_pid: str, yr_mth: () = None):
    """grabs all the shows ever played for a Broadcast
    
    Returns
        List of shows pid
    """
    
    show_list = []
    
    if yr_mth is None:
        calendar = ss.get_show_calendar(broadcast_pid)
        for yr in calendar:
                for mth in calendar[yr]:
                    show_list.extend(ss.get_shows_in_mth(broadcast_pid,yr,mth))
    else:
        show_list.extend(ss.get_shows_in_mth(broadcast_pid, yr_mth[0],yr_mth[1]))
    return show_list

def broadcasts_in_db():
    bro = Broadcast.query.all()
    return(bro)

def showsToGrab():
    """Checks DB for the Broadcast then grabs all the shows of that brocadcast and
    then checks that the shows exist in the DB if they don't then grabs the show
    
    Returns:
        [type] -- [description]
    """
    bro = broadcasts_in_db()
    broadcast_dict = {}

    for b in bro:
        broadcast_dict[b.pid] = grab_all_show_pid(b.pid)
        

    #  ------------------ compare to what is in the db and then grab all the shows no there

    

    return broadcast_dict

    


def add_show(pid):
    print("test")


def add_track():
    """add track to the db
    """
    print("test")


    