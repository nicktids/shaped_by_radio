import requests
import urllib
import json
import lxml.html
from lxml import etree
import logging
from bs4 import BeautifulSoup
import pandas as pd


def get_show_calendar(broadcast_pid, api_url='http://clifton.api.bbci.co.uk', calendar="/aps/programmes/{pid}/episodes.json"):
    '''
    for a given broadcaster returns a dictionary of the years and 
    months a given broadcast show has been on.
    
    Parameters
    ----------
    broadcast_pid : the shows underlying pid
    
    api_url : bbc api as of 2019
    
    calendar = the api string that gets all the json for the years and months
    
    Returns
    -------
    Dictionary of Year and the Months in the year the show plays
    
    '''
    
    episodes = url + calendar.format(pid=broadcast_pid)
    print(episodes)
    all_episodes = session.get(episodes).json()

    hist_mth_yr ={}
    ls = []

    for yr in all_episodes["filters"]["years"]:
    #     print(x["id"])
        mth_list = yr["months"]
        hist_mth_yr[yr['id']] = [mth["id"] for mth in yr['months']]

    return hist_mth_yr