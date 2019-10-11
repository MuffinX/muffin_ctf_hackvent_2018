#!/usr/bin/env python3

import os
import sys
import hashlib
import _thread
import socket

from tornado.tcpserver import TCPServer
import tornado.httpclient
from tornado.iostream import StreamClosedError
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.netutil import *
from tornado.web import *
import tornado.web

import requests

from database import *

# NUMBER_OF_REQUESTS_TICK = 5

ATTACK_POINTS_PER_ATTACK = 20

TUNNEL_SOCKETS = {}


def tunnel_recv_auth_token(tunnel_socket, tunnel_addr):
    global TUNNEL_SOCKETS

    try:
        # recieve auth token
        auth_json = tunnel_socket.recv(4096)
        auth_json = auth_json.decode('utf-8')
        auth_json  = json.loads(auth_json)

        # get player
        auth_token = auth_json['AUTH_TOKEN']
        db_player = get_player_by_auth_token(auth_token)


        if(db_player != None):

            print('[+] New tunnel connection from player {0}'.format(db_player.name))

            # add player tunnel socket to TUNNEL_SOCKETS
            if db_player.name in TUNNEL_SOCKETS.keys():
                try:
                    TUNNEL_SOCKETS[db_player.name]['socket'].close()
                except: pass

                del TUNNEL_SOCKETS[db_player.name]


            TUNNEL_SOCKETS[db_player.name] = {
                'socket' : tunnel_socket,
                'queue' : []
            }
    except: pass

def tunnel_accept_connections():
    while True:
        try:
            # start new thread for recvieving auth tokens
            tunnel_socket, tunnel_addr = tunnel_server.accept()
            tunnel_socket.settimeout(4)
            _thread.start_new_thread(tunnel_recv_auth_token, (tunnel_socket, tunnel_addr,  ) )
        except: pass


tunnel_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tunnel_server.bind(('0.0.0.0', 9181))
tunnel_server.settimeout(4)
tunnel_server.listen(1)

# accept tunnel connections
_thread.start_new_thread(tunnel_accept_connections, ( ) )





def tunnel_access_handle_connection(tunnel_access_socket, tunnel_access_addr):
    global TUNNEL_SOCKETS

    try:
        last_tick = get_last_db_tick()
        if last_tick != None:
            current_tick = last_tick.tick

            http_request = tunnel_access_socket.recv(4096).decode('utf-8')
            http_headers = http_request[:http_request.index('\r\n\r\n')].split('\r\n')
            http_body = http_request[http_request.index('\r\n\r\n')+4:]

            http_method = http_headers[0].split(' ')[0]
            http_path = http_headers[0].split(' ')[1]

            if http_path.count('/') >= 3:
                target_player = http_path.split('/')[1]
                target_service = http_path.split('/')[2]

                for i in range(2):
                    http_path = http_path[http_path.index('/')+1:]

                http_path = '/' + http_path

                new_request = http_method + ' ' + http_path + ' HTTP/1.0\r\n'
                new_request += 'Host: 0.0.0.0:80\r\n'

                #exclude_headers = ['Host: ', 'User-Agent: ', 'Connection: ', 'Accept-Encoding: ', 'Accept: ']
                exclude_headers = ['Host', 'User-Agent']

                for http_header in http_headers[1:]:
                    excluded = False
                    for exclude_header in exclude_headers:
                        if exclude_header in http_header: excluded = True

                    if excluded == False:
                        new_request += http_header + '\r\n'

                new_request += '\r\n'
                new_request += http_body

                if target_player in TUNNEL_SOCKETS.keys():

                    curr_random_hash = hashlib.md5(os.urandom(16)).hexdigest()
                    TUNNEL_SOCKETS[target_player]['queue'].append(curr_random_hash)

                    tunnel_socket = TUNNEL_SOCKETS[target_player]['socket']
                    tunnel_answer = ''

                    while True:
                        if TUNNEL_SOCKETS[target_player]['queue'][0] == curr_random_hash:

                            tunnel_answer = ''

                            try:
                                #print('[+] Sending to player {0} :'.format(target_player))
                                #print(str(new_request.encode('utf-8')))
                                tunnel_socket.send(new_request.encode('utf-8'))
                                #print('[+] Recieved from player {0} :'.format(target_player))
                                tunnel_answer = tunnel_socket.recv(4096)
                                #print(str(tunnel_answer))
                            except Exception as e:
                                #print('tunnel_socket error: ' + str(e))
                                pass


                            # fix content-length
                            # try:
                            #     if tunnel_answer.index(b'Content-Length: ') > -1:
                            #
                            #         tunnel_answer_body = tunnel_answer[tunnel_answer.rindex(b'\r\n\r\n')+4:]
                            #
                            #         new_content_length = len(tunnel_answer_body)
                            #
                            #         rest_headers = tunnel_answer[tunnel_answer.index(b'Content-Length: ')+len(b'Content-Length: '):]
                            #         rest_headers = rest_headers[rest_headers.index(b'\r\n'):]
                            #         rest_headers = rest_headers[:rest_headers.rindex(b'\r\n\r\n')]
                            #
                            #         new_tunnel_answer = tunnel_answer[:tunnel_answer.index(b'Content-Length: ')]
                            #         new_tunnel_answer += b'Content-Length: ' + str(new_content_length).encode('utf-8') + b'\r\n'
                            #         new_tunnel_answer += rest_headers + b'\r\n\r\n' + tunnel_answer_body
                            #
                            #         tunnel_answer = new_tunnel_answer
                            # except Exception as e:
                            #     #print('Fix Content-Len Error: ' + str(e))
                            #     pass


                            try:
                                tunnel_access_socket.send(tunnel_answer)
                            except Exception as e:
                                print('Tunnel Access Send Error: ' + str(e))

                            TUNNEL_SOCKETS[target_player]['queue'].remove(curr_random_hash)
                            break

        tunnel_access_socket.close()
    except Exception as e:
        #print('General Error: ' + str(e))
        pass

def tunnel_access_accept_connections():
    while True:
        try:
            # start new thread for recvieving access socket
            tunnel_access_socket, tunnel_access_addr = tunnel_access_server.accept()
            tunnel_access_socket.settimeout(4)
            _thread.start_new_thread(tunnel_access_handle_connection, (tunnel_access_socket, tunnel_access_addr,  ) )
        except: pass


tunnel_access_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tunnel_access_server.bind(('0.0.0.0', 9182))
tunnel_access_server.settimeout(4)
tunnel_access_server.listen(1)

_thread.start_new_thread(tunnel_access_accept_connections, ( ) )





class APIGetPlayers(tornado.web.RequestHandler):
    def post(self):
        self.write(
            tornado.escape.json_encode({
                'players' : [player_name for player_name in TUNNEL_SOCKETS.keys()]
            })
        )



class APIPostFlags(tornado.web.RequestHandler):
    def post(self):
        try:
            # player flag submit
            last_tick = get_last_db_tick()

            if last_tick != None:
                current_tick = last_tick.tick

                # get player by auth token
                post_data = tornado.escape.json_decode(self.request.body)
                auth_token = post_data['AUTH_TOKEN']

                db_attacker = get_player_by_auth_token(auth_token)
                if db_attacker != None:
                    # loop through submitted flags
                    submitted_flags = post_data['flags']
                    flag_results = []

                    for submit_flag in submitted_flags:
                        flag_submit_result = 'flag_submitted'

                        # check flags and set flag result
                        get_player_service_by_flag_session = session()
                        player_service = get_player_service_by_flag_session.query(PlayerService).filter(
                            PlayerService.flag == submit_flag
                        ).filter(
                            PlayerService.player_id != db_attacker.id
                        ).first()

                        get_player_service_by_flag_session.close()

                        if player_service == None: flag_submit_result = 'flag_not_found'
                        elif player_service.tick_id != current_tick:
                            flag_submit_result = 'flag_too_old'
                        else:
                            check_if_flag_already_exists_session = session()
                            already_submitted_flag = check_if_flag_already_exists_session.query(FlagsStolen).filter(
                                FlagsStolen.player_service_id == player_service.id
                            ).filter(
                                FlagsStolen.attacker_id == db_attacker.id
                            ).first()
                            check_if_flag_already_exists_session.close()

                            add_flag_session = session()
                            if already_submitted_flag == None:
                                # add flag
                                add_flag_session.add(FlagsStolen(
                                    player_service_id = player_service.id,
                                    attacker_id = db_attacker.id
                                ))

                                # increase attack points
                                attacked_service_id = player_service.service_id

                                attacker_player_service = add_flag_session.query(PlayerService).filter(
                                    PlayerService.service_id == attacked_service_id
                                ).filter(
                                    PlayerService.player_id == db_attacker.id
                                ).order_by(
                                    PlayerService.tick_id.desc()
                                ).first()

                                attacker_player_service.attack_points = attacker_player_service.attack_points + ATTACK_POINTS_PER_ATTACK

                                add_flag_session.commit()
                                add_flag_session.close()
                            else:
                                flag_submit_result = 'flag_already_submitted'

                        flag_results.append({
                            'flag' : submit_flag,
                            'result' : flag_submit_result
                        })

                    self.write(
                        tornado.escape.json_encode({
                            'results' : flag_results
                        })
                    )
        except Exception as e:
            pass



# start api server
api_server = tornado.web.Application([
    (r'/api/get_players', APIGetPlayers),
    (r'/api/post_flags', APIPostFlags),
])


api_server.listen(9180)

IOLoop.current().start()
