import sqlalchemy
from dynaconf import settings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I_love_MAH'
    
    DB_URL = f'postgresql+psycopg2://{settings.USERNAME}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.DATABASE}'
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
