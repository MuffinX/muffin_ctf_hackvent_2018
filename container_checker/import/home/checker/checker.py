#!/usr/bin/env python

import hashlib
import os
import sys
from threading import Thread

from database import *
import time


import requests
from bakery import *
from garden import *
from mill import *
from port import *
from barracks import *
from keep import *


API_URL = 'http://api:9182'


def generate_tunnel_url(player, service):
    return ('{0}/{1}/{2}/'.format(API_URL, player, service))

def gen_random_flag(): return ('muffinCTF{' + hashlib.sha1(os.urandom(32)).hexdigest() + '}')


TUNNEL_PLAYERS = []
def get_tunnel_players():
    global TUNNEL_PLAYERS

    while True:
        try:
            TUNNEL_PLAYERS = requests.post(
                'http://api:9180/api/get_players'
            ).json()['players']

            time.sleep(120)
        except Exception as e:
            print(str(e))



def bakery_checker():
    while True:
        try:
            check_service_session = session()
            last_tick = get_last_db_tick()


            if last_tick != None:
                db_player_services = check_service_session.query(Player, Service, PlayerService).filter(
                    PlayerService.player_id == Player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    PlayerService.tick_id == last_tick.tick
                ).filter(
                    Service.name == 'bakery'
                ).filter(
                    PlayerService.status == 'NOT_CHECKED'
                ).all()

                for db_player_service in db_player_services:
                    service_status = 'OFF'

                    if db_player_service.Player.name in TUNNEL_PLAYERS:
                        tunnel_url = generate_tunnel_url(db_player_service.Player.name, 'bakery')

                        service_status = check_bakery(
                            tunnel_url,
                            db_player_service.PlayerService.flag
                        )

                    db_player_service.PlayerService.status = service_status
                    check_service_session.commit()

            check_service_session.close()

        except Exception as e:
            pass
            #sys.stderr.write(str(e))



def garden_checker():
    while True:
        try:
            check_service_session = session()
            last_tick = get_last_db_tick()


            if last_tick != None:
                db_player_services = check_service_session.query(Player, Service, PlayerService).filter(
                    PlayerService.player_id == Player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    PlayerService.tick_id == last_tick.tick
                ).filter(
                    Service.name == 'garden'
                ).filter(
                    PlayerService.status == 'NOT_CHECKED'
                ).all()

                for db_player_service in db_player_services:
                    service_status = 'OFF'

                    if db_player_service.Player.name in TUNNEL_PLAYERS:
                        tunnel_url = generate_tunnel_url(db_player_service.Player.name, 'garden')

                        service_status = check_garden(
                            tunnel_url,
                            db_player_service.PlayerService.flag
                        )

                    db_player_service.PlayerService.status = service_status
                    check_service_session.commit()

            check_service_session.close()

        except Exception as e:
            pass
            #sys.stderr.write(str(e))


def mill_checker():
    while True:
        try:
            check_service_session = session()
            last_tick = get_last_db_tick()


            if last_tick != None:
                db_player_services = check_service_session.query(Player, Service, PlayerService).filter(
                    PlayerService.player_id == Player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    PlayerService.tick_id == last_tick.tick
                ).filter(
                    Service.name == 'mill'
                ).filter(
                    PlayerService.status == 'NOT_CHECKED'
                ).all()

                for db_player_service in db_player_services:
                    service_status = 'OFF'

                    if db_player_service.Player.name in TUNNEL_PLAYERS:
                        tunnel_url = generate_tunnel_url(db_player_service.Player.name, 'mill')

                        service_status = check_mill(
                            tunnel_url,
                            db_player_service.PlayerService.flag
                        )

                    db_player_service.PlayerService.status = service_status
                    check_service_session.commit()

            check_service_session.close()

        except Exception as e:
            pass
            #sys.stderr.write(str(e))


def port_checker():
    while True:
        try:
            check_service_session = session()
            last_tick = get_last_db_tick()


            if last_tick != None:
                db_player_services = check_service_session.query(Player, Service, PlayerService).filter(
                    PlayerService.player_id == Player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    PlayerService.tick_id == last_tick.tick
                ).filter(
                    Service.name == 'port'
                ).filter(
                    PlayerService.status == 'NOT_CHECKED'
                ).all()

                for db_player_service in db_player_services:
                    service_status = 'OFF'

                    if db_player_service.Player.name in TUNNEL_PLAYERS:
                        tunnel_url = generate_tunnel_url(db_player_service.Player.name, 'port')

                        service_status = check_port(
                            tunnel_url,
                            db_player_service.PlayerService.flag
                        )

                    db_player_service.PlayerService.status = service_status
                    check_service_session.commit()

            check_service_session.close()

        except Exception as e:
            pass
            #sys.stderr.write(str(e))

def barracks_checker():
    while True:
        try:
            check_service_session = session()
            last_tick = get_last_db_tick()


            if last_tick != None:
                db_player_services = check_service_session.query(Player, Service, PlayerService).filter(
                    PlayerService.player_id == Player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    PlayerService.tick_id == last_tick.tick
                ).filter(
                    Service.name == 'barracks'
                ).filter(
                    PlayerService.status == 'NOT_CHECKED'
                ).all()

                for db_player_service in db_player_services:
                    service_status = 'OFF'

                    if db_player_service.Player.name in TUNNEL_PLAYERS:
                        tunnel_url = generate_tunnel_url(db_player_service.Player.name, 'barracks')

                        service_status = check_barracks(
                            tunnel_url,
                            db_player_service.PlayerService.flag
                        )

                    db_player_service.PlayerService.status = service_status
                    check_service_session.commit()

            check_service_session.close()

        except Exception as e:
            pass
            #sys.stderr.write(str(e))

def keep_checker():
    while True:
        try:
            check_service_session = session()
            last_tick = get_last_db_tick()


            if last_tick != None:
                db_player_services = check_service_session.query(Player, Service, PlayerService).filter(
                    PlayerService.player_id == Player.id
                ).filter(
                    PlayerService.service_id == Service.id
                ).filter(
                    PlayerService.tick_id == last_tick.tick
                ).filter(
                    Service.name == 'keep'
                ).filter(
                    PlayerService.status == 'NOT_CHECKED'
                ).all()

                for db_player_service in db_player_services:
                    service_status = 'OFF'

                    if db_player_service.Player.name in TUNNEL_PLAYERS:
                        tunnel_url = generate_tunnel_url(db_player_service.Player.name, 'keep')

                        service_status = check_keep(
                            tunnel_url,
                            db_player_service.PlayerService.flag
                        )

                    db_player_service.PlayerService.status = service_status
                    check_service_session.commit()

            check_service_session.close()

        except Exception as e:
            pass
            #sys.stderr.write(str(e))





def update_scoring():
    while True:
        update_scoring_session = session()

        last_tick = get_last_db_tick()

        db_player_services = update_scoring_session.query(PlayerService, Tick).filter(
            PlayerService.tick_id == Tick.tick
        ).filter(
            PlayerService.tick_id > (last_tick.tick - 2)
        ).filter(
            PlayerService.status == 'ON'
        ).all()

        for db_player_service in db_player_services:
            try:

                inc_availability = 0
                inc_defense = 0

                db_player_service_flags_stolen = update_scoring_session.query(FlagsStolen).filter(
                    FlagsStolen.player_service_id == db_player_service.PlayerService.id
                ).count()

                inc_availability = db_player_service.Tick.number_of_players
                inc_defense = db_player_service.Tick.number_of_players - db_player_service_flags_stolen

                if inc_availability > 0 and inc_defense > 0:
                    #print('Updating {0}'.format(str(db_player_service.PlayerService.id)))
                    #print(str(db_player_service.Tick.tick))
                    #print('inc_availability = {0}'.format(str(inc_availability)))
                    #print('inc_defense = {0}'.format(str(inc_defense)))

                    # update current scoring
                    db_player_service.PlayerService.availability_points = db_player_service.PlayerService.old_availability_points + inc_availability
                    db_player_service.PlayerService.defense_points = db_player_service.PlayerService.old_defense_points + inc_defense


            except Exception as e:
                print(str(e))

        update_scoring_session.commit()
        update_scoring_session.close()



@event.listens_for(Tick, 'after_insert')
def clean_database(mapper, connection, target):
    curr_tick = target.tick

    clean_database_session = sessionmaker(bind=connection)()

    # delete tunnel_requests
    clean_database_session.query(TunnelRequest).filter(
        TunnelRequest.tick_id != curr_tick
    ).delete()
    clean_database_session.commit()

    db_tick_to_delete_before = clean_database_session.query(Tick).order_by(
        Tick.tick.desc()
    ).all()

    if(len(db_tick_to_delete_before)) > 5:
        db_tick_to_delete_before = db_tick_to_delete_before[4]

        if db_tick_to_delete_before != None:

            clean_flags = clean_database_session.query(FlagsStolen, PlayerService, Tick).filter(
                FlagsStolen.player_service_id == PlayerService.id
            ).filter(
                PlayerService.tick_id == Tick.tick
            ).filter (
                Tick.tick < db_tick_to_delete_before.tick
            ).all()

            for clean_flag in clean_flags:
                clean_database_session.delete(clean_flag.FlagsStolen)
            clean_database_session.commit()

            clean_player_services = clean_database_session.query(PlayerService, Tick).filter(
                PlayerService.tick_id == Tick.tick
            ).filter (
                Tick.tick < db_tick_to_delete_before.tick
            ).all()


            for clean_player_service in clean_player_services:
                clean_database_session.delete(clean_player_service.PlayerService)
            clean_database_session.commit()

            clean_database_session.query(Tick).filter(
                Tick.tick < db_tick_to_delete_before.tick
            ).delete()
            clean_database_session.commit()

    clean_database_session.close()




@event.listens_for(Tick, 'after_insert')
def create_player_services(mapper, connection, target):
    tick_inserted = target

    # create player sessions
    create_player_services_session = sessionmaker(bind=connection)()

    # check if tick exists
    db_players = create_player_services_session.query(Player).all()
    db_services = create_player_services_session.query(Service).all()

    for db_player in db_players:
        for db_service in db_services:
            # add player service

            previous_player_service = create_player_services_session.query(PlayerService).filter(
                PlayerService.player_id == db_player.id
            ).filter(
                PlayerService.service_id == db_service.id
            ).filter(
                PlayerService.tick_id < tick_inserted.tick
            ).order_by(
                PlayerService.tick_id.desc()
            ).first()

            old_attack_points = 0
            old_defense_points = 0
            old_availability_points = 0

            if previous_player_service != None:
                old_attack_points = (previous_player_service.attack_points if previous_player_service.attack_points > previous_player_service.old_attack_points else previous_player_service.old_attack_points)
                old_defense_points = (previous_player_service.defense_points if previous_player_service.defense_points > previous_player_service.old_defense_points else previous_player_service.old_defense_points)
                old_availability_points = (previous_player_service.availability_points if previous_player_service.availability_points > previous_player_service.old_availability_points else previous_player_service.old_availability_points)



            create_player_services_session.add(
                PlayerService(
                    player_id = db_player.id,
                    service_id = db_service.id,
                    tick_id = tick_inserted.tick,
                    status = 'NOT_CHECKED',
                    attack_points = old_attack_points,
                    old_attack_points = old_attack_points,
                    defense_points = old_defense_points,
                    old_defense_points = old_defense_points,
                    availability_points = old_availability_points,
                    old_availability_points = old_availability_points,
                    flag = gen_random_flag()
                )
            )


    create_player_services_session.commit()
    create_player_services_session.close()



def create_ticks():
    while True:
        try:
            create_ticks_session = session()
            curr_tick = get_current_tick()

            db_tick = create_ticks_session.query(Tick).filter(Tick.tick == curr_tick).first()
            number_of_players = len(create_ticks_session.query(Player).all())

            if db_tick == None:
                # add new tick
                create_ticks_session.add(
                    Tick(
                        tick = curr_tick,
                        number_of_players = number_of_players
                    )
                )

                create_ticks_session.commit()
            else:
                if number_of_players != db_tick.number_of_players:
                    db_tick.number_of_players = number_of_players
                    create_ticks_session.commit()

            create_ticks_session.close()
        except Exception as e:
            pass
            #sys.stderr.write(str(e))



# create ticks
thread_create_ticks = Thread(target=create_ticks)
thread_update_scoring = Thread(target=update_scoring)
thread_create_ticks.start()
thread_update_scoring.start()


# player service checkers
thread_get_tunnel_players = Thread(target=get_tunnel_players)
thread_bakery_checker = Thread(target=bakery_checker)
thread_garden_checker = Thread(target=garden_checker)
thread_mill_checker = Thread(target=mill_checker)
thread_port_checker = Thread(target=port_checker)
thread_barracks_checker = Thread(target=barracks_checker)
thread_keep_checker = Thread(target=keep_checker)

thread_get_tunnel_players.start()
thread_bakery_checker.start()
thread_garden_checker.start()
thread_mill_checker.start()
thread_port_checker.start()
thread_barracks_checker.start()
thread_keep_checker.start()
