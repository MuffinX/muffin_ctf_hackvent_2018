#!/usr/bin/env python

import time
import os
import hashlib
import json
import thread
from datetime import datetime
from datetime import timedelta

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

# APP Settings
APP_SECRET_KEY = '4558c0af0b5d2dcef844399d1f285a58c1419ef9c8acbc4337c3db8dda04a8cde2d314ab0ae98a0d7904d013763126dca1f3d8ab59af3c59d6ccc359ed3c6d45'

# CTF Settings
CTF_START = datetime(2018, 11, 4, 20, 0, 0, 0)

# MYSQL Settings
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'e2095f3411655f735d4d8552ef8c973268d77d49d7a404eaa8b7b14525963d52'
MYSQL_HOST = 'database'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'muffin_ctf'

app = Flask(__name__, static_url_path='/static')
app.secret_key = APP_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql://{0}:{1}@{2}:{3}/{4}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    auth_token = db.Column(db.String(64), unique=True, nullable=False)

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)

class Tick(db.Model):
    __tablename__ = 'ticks'
    tick = db.Column(db.Integer, primary_key=True)
    number_of_players = db.Column(db.Integer, nullable=False)

class TunnelRequest(db.Model):
    __tablename__ = 'tunnel_requests'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    tick_id = db.Column(db.Integer, db.ForeignKey('ticks.tick'), nullable=False)
    ip = db.Column(db.String(32), nullable=False)

class PlayerService(db.Model):
    __tablename__ = 'player_services'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    tick_id = db.Column(db.Integer, db.ForeignKey('ticks.tick'), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    attack_points = db.Column(db.Integer, nullable=False)
    old_attack_points = db.Column(db.Integer, nullable=False)
    defense_points = db.Column(db.Integer, nullable=False)
    old_defense_points = db.Column(db.Integer, nullable=False)
    availability_points = db.Column(db.Integer, nullable=False)
    old_availability_points = db.Column(db.Integer, nullable=False)
    flag = db.Column(db.String(51), unique=True, nullable=False)


class FlagsStolen(db.Model):
    __tablename__ = 'submitted_flags'
    id = db.Column(db.Integer, primary_key=True)
    player_service_id = db.Column(db.Integer, db.ForeignKey('player_services.id'), nullable=False)
    attacker_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)



def get_current_tick():
    current_tick = (time.time() - time.mktime(CTF_START.timetuple()))
    current_tick = current_tick / 180
    return int(current_tick)


def get_last_db_tick():
     return db.session.query(Tick).order_by(Tick.tick.desc()).first()

def get_player_by_auth_token(auth_token):
    players_found = (Player.query.filter(Player.auth_token == auth_token).all())
    if len(players_found) > 0: return players_found[0]
    return None


if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    # services
    db.session.add(Service(id = 1, name = 'bakery'))
    db.session.add(Service(id = 2, name = 'garden'))
    db.session.add(Service(id = 3, name = 'mill'))
    db.session.add(Service(id = 4, name = 'port'))
    db.session.add(Service(id = 5, name = 'barracks'))
    db.session.add(Service(id = 6, name = 'keep'))

    db.session.commit()
