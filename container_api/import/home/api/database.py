import time
import os
import hashlib
import json
from datetime import datetime
from datetime import timedelta

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.orm import sessionmaker


# CTF Settings
CTF_START = datetime(2018, 11, 4, 20, 0, 0, 0)

# MYSQL Settings
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'e2095f3411655f735d4d8552ef8c973268d77d49d7a404eaa8b7b14525963d52'
MYSQL_HOST = 'database'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'muffin_ctf'
MYSQL_URL = ('mysql://{0}:{1}@{2}:{3}/{4}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))

engine = create_engine(MYSQL_URL, echo=False)
Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    auth_token = Column(String(64), unique=True, nullable=False)

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)

class PlayerService(Base):
    __tablename__ = 'player_services'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    tick_id = Column(Integer, ForeignKey('ticks.tick'), nullable=False)
    status = Column(String(32), nullable=False)
    attack_points = Column(Integer, nullable=False)
    old_attack_points = Column(Integer, nullable=False)
    defense_points = Column(Integer, nullable=False)
    old_defense_points = Column(Integer, nullable=False)
    availability_points = Column(Integer, nullable=False)
    old_availability_points = Column(Integer, nullable=False)
    flag = Column(String(51), unique=True, nullable=False)

class Tick(Base):
    __tablename__ = 'ticks'
    tick = Column(Integer, primary_key=True)
    number_of_players = Column(Integer, nullable=False)

class FlagsStolen(Base):
    __tablename__ = 'submitted_flags'
    id = Column(Integer, primary_key=True)
    player_service_id = Column(Integer, ForeignKey('player_services.id'), nullable=False)
    attacker_id = Column(Integer, ForeignKey('players.id'), nullable=False)

class TunnelRequest(Base):
    __tablename__ = 'tunnel_requests'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    tick_id = Column(Integer, nullable=False)
    ip = Column(String(32), nullable=False)


def get_current_tick():
    current_tick = (time.time() - time.mktime(CTF_START.timetuple()))
    current_tick = current_tick / 180
    return int(current_tick)


def get_last_db_tick():
    get_last_tick_session = session()
    last_tick = get_last_tick_session.query(Tick).order_by(Tick.tick.desc()).first()
    get_last_tick_session.close()

    return last_tick

def get_player_by_auth_token(auth_token):
    player_by_auth_token_session = session()
    players_found = player_by_auth_token_session.query(Player).filter(Player.auth_token == auth_token).all()
    player_by_auth_token_session.close()
    if len(players_found) > 0: return players_found[0]
    return None
