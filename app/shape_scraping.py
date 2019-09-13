import requests
import json
import logging
import pandas as pd

from dynaconf import settings

# api help from https://get-iplayer.infradead.narkive.com/fcULS8EM/bbc-programmes-api-json-feeds
# https://github.com/bbc/programmes-clifton/blob/master/app/config/routing.yml

session = requests.Session()


def get_show_calendar(broadcast_pid, session=session,
                      api_url=settings.API.PREFIX,
                      calendar=settings.API.PID_EPISODES):
    '''
    for a given broadcaster returns a dictionary of the years and 
    months a given broadcast show has been on.

    Parameters
    ----------
    broadcast_pid : the shows underlying pid

    session : Requests session

    api_url : bbc api as of 2019

    calendar = the api string that gets all the json for the years and months

    Returns
    -------
    Dictionary of Year and the Months in the year the show plays

    '''

    episodes = api_url + calendar.format(pid=broadcast_pid)
    print(episodes)
    all_episodes = session.get(episodes).json()

    hist_mth_yr = {}
    ls = []

    for yr in all_episodes["filters"]["years"]:
        #     print(x["id"])
        mth_list = yr["months"]
        hist_mth_yr[yr['id']] = [mth["id"] for mth in yr['months']]

    return hist_mth_yr


def get_shows_in_mth(broadcast_pid, year, mth, session=session,
                     api_url=settings.API.PREFIX,
                     api_mth=setting.API.PID_LIST_YR_MTH):
    '''
    Function that takes the Broadcaster/show, Year (int) and Month (int 1=Jan 12=Dec) 
    and returns list of shows


    Parameters
    ----------
    broadcast_pid : the shows underlying pid
    year : year
    mth : month

    session : Requests session

    api_url : bbc api as of 2019

    calendar = the api string that gets all the json for the years and months

    Returns
    -------
    list of shows_pids for the month and year in question

    '''
    show_dic = {}
    ep_in_mth_url = api_url + \
        api_mth.format(pid=broadcast_pid, year=year, month=mth)
#     print(ep_in_mth_url)
    show_json = session.get(ep_in_mth_url).json()
    shows_pid = []

    for x in show_json['broadcasts']:
        shows_pid.append(x['programme']['pid'])

    return shows_pid


def get_show_details(episode_pid, session=session,
                     api_url=settings.API.PREFIX,
                     api_ep=settings.API.PID_SHOW,
                     ):
    '''
    Parameters
    ----------
    episode_pid : the shows underlying pid

    Returns
    ----------

    df of the show table to upload.
    '''

    ep_url = api_url + api_ep.format(pid=episode_pid)
    ep_json = session.get(ep_url).json()

    show = {}

    x = ep_json['programme']
    show['date'] = x['first_broadcast_date']
    show['pid'] = x['pid']
    show['title'] = x['title']
    show['desc_shoty'] = x['short_synopsis']
    show['desc_med'] = x['medium_synopsis']
    show['desc_long'] = x['long_synopsis']
    show['image_pid'] = x['image']['pid']

    return show


def get_episode_tracks(episode_pid, session=session,
                       api_url=settings.API.PREFIX,
                       api_ep_tracks=settings.API.PID_SEGMENTS
                       ):
    tracks_url = api_url + api_ep_tracks.format(pid=episode_pid)
    tracks_json = session.get(tracks_url).json()

    df_tr = pd.DataFrame.from_dict(tr['segment_events'])
    df_tr.rename(columns={'pid': "bbctrack_position_pid",
                          'position': 'show_position',
                          'version_offset': 'show_offset',
                          'title': 'special_title'}, inplace=True)

    df_tr1 = pd.DataFrame(df_tr.segment.tolist())

    df_artist = df_artist = pd.DataFrame(df_tr1.primary_contributor.tolist())
    df_artist.rename(columns={"pid": "bbc_artist_pid"}, inplace=True)

    df_track = df_tr_temp[['track_title', 'duration', 'pid']]
    df_track.rename(columns={"pid": "bbc_track_pid"},inplace=True)

    df_pos = df_tr[['show_position', 'show_offset', 'special_title']]

    df_all = pd.concat([df_artist, df_track, df_pos], axis=1)

    return tracks_json
