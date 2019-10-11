#!/usr/bin/env python

import time
import os
import hashlib
import json
import thread
import base64
from datetime import datetime
from datetime import timedelta
import operator
import sys
import requests

from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.serving import run_simple

from Crypto.PublicKey import RSA

from database import *


SERVER_PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''

SERVER_PRIVATE_KEY = RSA.importKey(SERVER_PRIVATE_KEY)



def rsa_decrypt(data):
    dec_data = ''
    try: dec_data = SERVER_PRIVATE_KEY.decrypt(data)
    except: pass
    return dec_data


# GUI
@app.route('/', methods=['GET'])
def index(): return render_template('index.html', user = session.get('user'))

@app.route('/home', methods=['GET'])
def home(): return render_template('home.html')

@app.route('/news', methods=['GET'])
def news(): return render_template('news.html')

@app.route('/visualization', methods=['GET'])
def visualization(): return render_template('visualization.html')

@app.route('/story', methods=['GET'])
def story():
    curr_path = os.path.realpath(__file__)
    curr_path = curr_path[:curr_path.rindex('/')]
    story = ''
    with open(curr_path + '/templates/story.html') as read_story: story = read_story.read()
    return story

@app.route('/how2play', methods=['GET'])
def how2play(): return render_template('how2play.html')

@app.route('/rules', methods=['GET'])
def rules(): return render_template('rules.html')

@app.route('/services', methods=['GET'])
def services(): return render_template('services.html')

cached_player_tunnels = []
cached_player_tunnels_tick = 0
player_tunnel_cache_run = False

def refresh_player_tunnels():
    global cached_player_tunnels
    global player_tunnel_cache_run

    try:
        cached_player_tunnels = requests.post(
            'http://api:9180/api/get_players'
        ).json()['players']
    except Exception as e:
        print(str(e))

    player_tunnel_cache_run = False

cached_scoreboard = []
cached_scoreboard_tick = 0

@app.route('/scoreboard', methods=['GET'])
def scoreboard():
    global cached_scoreboard
    global cached_scoreboard_tick
    global cached_player_tunnels
    global cached_player_tunnels_tick
    global player_tunnel_cache_run

    previous_tick = db.session.query(Tick).order_by(Tick.tick.desc()).all()


    if len(previous_tick) >= 2:
        previous_tick = previous_tick[1]

        if cached_player_tunnels_tick != previous_tick.tick and player_tunnel_cache_run == False:
            refresh_player_tunnels()
            cached_player_tunnels_tick = previous_tick.tick


        if previous_tick != None and cached_scoreboard_tick != previous_tick.tick:

            new_scoreboard = []

            players = db.session.query(Player).filter(
                Player.name != 'MuffinX'
            ).filter(
                Player.name != 'Kiwi.wolf'
            ).all()

            player_unsorted_by_score = []

            for player in players:
                player_services_dict = {
                    'name' : player.name,
                    'tunnel_connection' : (player.name in cached_player_tunnels),
                    'services' : {}
                }

                # get previous player service
                player_services = db.session.query(PlayerService, Service, Tick).filter(
                    PlayerService.player_id == player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    Tick.tick == PlayerService.tick_id
                ).filter(
                    PlayerService.tick_id == previous_tick.tick
                ).all()

                player_score = 0

                for player_service in player_services:
                    curr_service_name = player_service.Service.name
                    player_services_dict['services'][curr_service_name] = {}

                    curr_service_status = player_service.PlayerService.status

                    curr_attack_points = int(player_service.PlayerService.attack_points)
                    curr_inc_attack_points = curr_attack_points - int(player_service.PlayerService.old_attack_points)
                    if curr_inc_attack_points < 0: curr_inc_attack_points = 0

                    curr_defense_points = int(player_service.PlayerService.defense_points)
                    curr_inc_defense_points = curr_defense_points - int(player_service.PlayerService.old_defense_points)
                    if curr_inc_defense_points < 0: curr_inc_defense_points = 0

                    curr_availability_points = int(player_service.PlayerService.availability_points)
                    curr_inc_availability_points = curr_availability_points - int(player_service.PlayerService.old_availability_points)
                    if curr_inc_availability_points < 0: curr_inc_availability_points = 0

                    player_score += curr_attack_points + curr_defense_points + curr_availability_points


                    player_services_dict['services'][curr_service_name]['status'] = curr_service_status
                    if curr_service_status == 'ON':
                        player_services_dict['services'][curr_service_name]['status_color'] = 'green'
                    elif curr_service_status == 'CORRUPT':
                        player_services_dict['services'][curr_service_name]['status_color'] = 'orange'
                    else:
                        player_services_dict['services'][curr_service_name]['status_color'] = 'red'

                    player_services_dict['services'][curr_service_name]['attack_points'] = curr_attack_points
                    player_services_dict['services'][curr_service_name]['defense_points'] = curr_defense_points
                    player_services_dict['services'][curr_service_name]['availability_points'] = curr_availability_points
                    player_services_dict['services'][curr_service_name]['inc_attack_points'] = curr_inc_attack_points
                    player_services_dict['services'][curr_service_name]['inc_defense_points'] = curr_inc_defense_points
                    player_services_dict['services'][curr_service_name]['inc_availability_points'] = curr_inc_availability_points
                    player_services_dict['services'][curr_service_name]['old_attack_points'] = player_service.PlayerService.old_attack_points
                    player_services_dict['services'][curr_service_name]['old_defense_points'] = player_service.PlayerService.old_defense_points
                    player_services_dict['services'][curr_service_name]['old_availability_points'] = player_service.PlayerService.old_availability_points

                player_services_dict['score'] = player_score
                player_unsorted_by_score.append(player_services_dict)

            player_sorted_by_score = sorted(player_unsorted_by_score, key=lambda player_unsorted: player_unsorted['score'], reverse=True)
            for place in range(1, len(player_sorted_by_score)+1):
                player_sorted_by_score[place-1]['place'] = place

            cached_scoreboard = player_sorted_by_score
            #cached_scoreboard_tick = previous_tick.tick

    return render_template('scoreboard.html', scoreboard=cached_scoreboard, tick=previous_tick.tick, number_of_players=previous_tick.number_of_players, number_of_player_tunnels=len(cached_player_tunnels))

@app.route('/prizes', methods=['GET'])
def prizes(): return render_template('prizes.html')

@app.route('/about', methods=['GET'])
def about(): return render_template('about.html')

@app.route('/login', methods=['GET'])
def login():
    auth_token = request.args.get('auth_token')
    if auth_token:
        auth_token = rsa_decrypt(base64.b64decode(auth_token))

        if '[BEGIN_JSON]' in auth_token:
            auth_token = auth_token[auth_token.index('[BEGIN_JSON]')+len('[BEGIN_JSON]'):]
            auth_json = json.loads(auth_token)

            auth_timestamp = auth_json['timestamp']
            auth_user = auth_json['user']

            time_difference = time.time() - auth_timestamp
            # valid for 1 minute
            if time_difference <= 60:
                session['user'] = auth_user


                # check if player exists in database, if not: create
                db_player = db.session.query(Player).filter_by(
                    name = auth_user
                ).first()

                if db_player == None:
                    db.session.add(Player(
                        name = auth_user,
                        auth_token = hashlib.sha256(os.urandom(32)).hexdigest()
                    ))

                    db.session.commit()

                    # update current tick number of players
                    current_db_tick = db.session.query(Tick).filter_by(
                        tick = get_current_tick()
                    ).first()


                    number_of_players = len(db.session.query(Player).all())

                    if(current_db_tick == None):
                        db.session.add(Tick(
                            tick = get_current_tick(),
                            number_of_players = number_of_players
                        ))
                    else:
                        current_db_tick.number_of_players = number_of_players

                    db.session.commit()


    return redirect(url_for('index'))


@app.route('/flags_stats', methods=['GET'])
def flags_stats():

    if session.get('user'):

        db_player = db.session.query(Player).filter(
            Player.name == session.get('user')
        ).first()

        if db_player != None:

            stats_dict = {}

            # get previous player service
            player_services = db.session.query(PlayerService, Service, Tick).filter(
                PlayerService.player_id == db_player.id
            ).filter(
                PlayerService.service_id == Service.id
            ).filter(
                PlayerService.tick_id == Tick.tick
            ).order_by(
                PlayerService.tick_id.desc()
            ).limit(36).all()[6:]


            for player_service in player_services:
                curr_tick = int(player_service.PlayerService.tick_id)
                curr_number_players = int(player_service.Tick.number_of_players)
                curr_service_name = player_service.Service.name
                curr_service_status = player_service.PlayerService.status

                curr_attack_points = int(player_service.PlayerService.attack_points)
                curr_inc_attack_points = curr_attack_points - int(player_service.PlayerService.old_attack_points)
                if curr_inc_attack_points < 0: curr_inc_attack_points = 0

                curr_defense_points = int(player_service.PlayerService.defense_points)
                curr_inc_defense_points = curr_defense_points - int(player_service.PlayerService.old_defense_points)
                if curr_inc_defense_points < 0: curr_inc_defense_points = 0

                curr_availability_points = int(player_service.PlayerService.availability_points)
                curr_inc_availability_points = curr_availability_points - int(player_service.PlayerService.old_availability_points)
                if curr_inc_availability_points < 0: curr_inc_availability_points = 0

                if not curr_tick in stats_dict.keys():
                    stats_dict[curr_tick] = {
                        'score' : 0,
                        'flag_criteria' : False,
                        'services' : {},
                        'number_of_players' : curr_number_players
                    }
                if not curr_service_name in stats_dict[curr_tick]['services']:
                    stats_dict[curr_tick]['services'][curr_service_name] = {}

                stats_dict[curr_tick]['services'][curr_service_name]['status'] = curr_service_status
                if curr_service_status == 'ON':
                    stats_dict[curr_tick]['services'][curr_service_name]['status_color'] = 'green'
                elif curr_service_status == 'CORRUPT':
                    stats_dict[curr_tick]['services'][curr_service_name]['status_color'] = 'orange'
                else:
                    stats_dict[curr_tick]['services'][curr_service_name]['status_color'] = 'red'

                stats_dict[curr_tick]['services'][curr_service_name]['attack_points'] = curr_attack_points
                stats_dict[curr_tick]['services'][curr_service_name]['defense_points'] = curr_defense_points
                stats_dict[curr_tick]['services'][curr_service_name]['availability_points'] = curr_availability_points
                stats_dict[curr_tick]['services'][curr_service_name]['inc_attack_points'] = curr_inc_attack_points
                stats_dict[curr_tick]['services'][curr_service_name]['inc_defense_points'] = curr_inc_defense_points
                stats_dict[curr_tick]['services'][curr_service_name]['inc_availability_points'] = curr_inc_availability_points
                stats_dict[curr_tick]['score'] = stats_dict[curr_tick]['score'] + (curr_attack_points + curr_defense_points + curr_availability_points)
                stats_dict[curr_tick]['services'][curr_service_name]['old_attack_points'] = player_service.PlayerService.old_attack_points
                stats_dict[curr_tick]['services'][curr_service_name]['old_defense_points'] = player_service.PlayerService.old_defense_points
                stats_dict[curr_tick]['services'][curr_service_name]['old_availability_points'] = player_service.PlayerService.old_availability_points


            flags = []

            # day_1_criteria
            for curr_tick in stats_dict.keys():
                tick_stats = stats_dict[curr_tick]

                day_1_criteria = False
                for criteria_service in ['bakery', 'garden']:
                    if criteria_service in tick_stats['services'].keys():
                        criteria_service_stats = tick_stats['services'][criteria_service]

                        availability_criteria = criteria_service_stats['inc_availability_points'] == tick_stats['number_of_players']
                        defense_criteria = criteria_service_stats['inc_defense_points'] == tick_stats['number_of_players']
                        attack_criteria = criteria_service_stats['inc_attack_points'] > 0

                        if availability_criteria and defense_criteria and attack_criteria: day_1_criteria = True

                stats_dict[curr_tick]['day_1_criteria'] = day_1_criteria


            day_1_criteria_counter = 0
            for curr_tick in stats_dict.keys():
                tick_stats = stats_dict[curr_tick]

                if tick_stats['day_1_criteria'] == True: day_1_criteria_counter += 1


            if day_1_criteria_counter > 1:
                flags.append('HV18{muffinCTF{d4y_1_l3t_th3_g4m3s_b3g1n_st4y_c0v3r3d_f0r_m0r3_h4x_stuff}}')



            # day_2_criteria
            for curr_tick in stats_dict.keys():
                tick_stats = stats_dict[curr_tick]

                day_2_criteria = False
                for criteria_service in ['mill', 'port']:
                    if criteria_service in tick_stats['services'].keys():
                        criteria_service_stats = tick_stats['services'][criteria_service]

                        availability_criteria = criteria_service_stats['inc_availability_points'] == tick_stats['number_of_players']
                        defense_criteria = criteria_service_stats['inc_defense_points'] == tick_stats['number_of_players']
                        attack_criteria = criteria_service_stats['inc_attack_points'] > 20

                        if availability_criteria and defense_criteria and attack_criteria: day_2_criteria = True

                stats_dict[curr_tick]['day_2_criteria'] = day_2_criteria

            day_2_criteria_counter = 0
            for curr_tick in stats_dict.keys():
                tick_stats = stats_dict[curr_tick]

                if tick_stats['day_2_criteria'] == True: day_2_criteria_counter += 1


            if day_2_criteria_counter > 1:
                flags.append('HV18{muffinCTF{d4y_2_g0sh_y0ur_r34lly_pwn1n_th3_stuff_l3l_g00d_b0y_g0_4h34d}}')

            # day_3_criteria
            for curr_tick in stats_dict.keys():
                tick_stats = stats_dict[curr_tick]

                day_3_criteria = False
                for criteria_service in ['barracks', 'keep']:
                    if criteria_service in tick_stats['services'].keys():
                        criteria_service_stats = tick_stats['services'][criteria_service]

                        availability_criteria = criteria_service_stats['inc_availability_points'] == tick_stats['number_of_players']
                        defense_criteria = criteria_service_stats['inc_defense_points'] == tick_stats['number_of_players']
                        attack_criteria = criteria_service_stats['inc_attack_points'] > 20

                        if availability_criteria and defense_criteria and attack_criteria: day_3_criteria = True

                stats_dict[curr_tick]['day_3_criteria'] = day_3_criteria

            day_3_criteria_counter = 0
            for curr_tick in stats_dict.keys():
                tick_stats = stats_dict[curr_tick]

                if tick_stats['day_3_criteria'] == True: day_3_criteria_counter += 1


            if day_3_criteria_counter > 1:
                flags.append('HV18{muffinCTF{d4y_3_t3h_1337_b001s_g3t_4ll_d3m_gr0up13z_4nd_b0x3n}}')



            player_auth_token = db.session.query(Player).filter(
                Player.name == session.get('user')
            ).first().auth_token

            return render_template('flags_stats.html', player_stats=stats_dict, player_auth_token=player_auth_token, flags=flags)


@app.route('/regenerate_auth_token', methods=['GET'])
def regenerate_auth_token():
    if session.get('user'):
        db_player = db.session.query(Player).filter(
            Player.name == session.get('user')
        ).first()

        db_player.auth_token = hashlib.sha256(os.urandom(32)).hexdigest()

        db.session.commit()

        return redirect(url_for('flags_stats'))

cached_visualization = []
cached_visualization_tick = 0
@app.route('/get_visualization', methods=['GET'])
def get_visualization():
    global cached_visualization
    global cached_visualization_tick

    previous_tick = db.session.query(Tick).order_by(Tick.tick.desc()).all()

    if len(previous_tick) >= 2:
        previous_tick = previous_tick[1]

        if previous_tick != None and cached_visualization_tick != previous_tick.tick:

            db_players = db.session.query(Player).all()
            db_services = db.session.query(Service).all()

            new_players = []

            for db_player in db_players:

                player_services = []
                for db_service in db_services:
                    db_player_service = db.session.query(PlayerService).filter(
                        PlayerService.player_id == db_player.id
                    ).filter(
                        PlayerService.service_id == db_service.id
                    ).filter(
                        PlayerService.tick_id == previous_tick.tick
                    ).first()

                    if db_player_service != None:
                        db_flags = db.session.query(FlagsStolen, Player).filter(
                            FlagsStolen.player_service_id == db_player_service.id
                        ).filter(
                            FlagsStolen.attacker_id == Player.id
                        ).all()

                        attacked_by = []

                        for db_flag in db_flags:
                            attacked_by.append(db_flag.Player.name)


                        player_services.append({
                            'id' : db_service.id,
                            'status' : db_player_service.status,
                            'attacked_by' : attacked_by
                        })

                new_player = {
                    'name' : db_player.name,
                    'services' : player_services
                }

                new_players.append(new_player)

            new_visualization = {
                'players': new_players
            }

            cached_visualization = new_visualization
            cached_visualization_tick = previous_tick.tick

    return json.dumps(cached_visualization)


@app.route('/logout', methods=['GET'])
def logout():
   session.pop('user', None)
   return redirect(url_for('index'))


app.jinja_env.globals.update(sorted=sorted)


run_simple('0.0.0.0', 9280, app, threaded=True)
