
import socket
import hashlib
import urllib


def do_get_request(path, params):

    path += '?' + urllib.urlencode(params)

    req = 'GET {0} HTTP/1.0\r\n'.format(path)
    req += 'Host: 0.0.0.0:80\r\n'
    #req += 'Transfer-Encoding: gzip\r\n'
    req += '\r\n\r\n'

    req_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    req_socket.connect(('api', 9182))
    req_socket.settimeout(4)

    req_socket.send(req)
    ret_data = req_socket.recv(4096)
    req_socket.close()
    return ret_data


def check_barracks(tunnel_url, flag):

    return_status = 'OFF'

    try:
        target_path = tunnel_url.replace('http://api:9182','')
        flag_md5 = hashlib.md5(flag).hexdigest()

        deploy_flag_answer = do_get_request(
            target_path + 'ak',
            {
                'n' : flag_md5, 'k' : flag
            }
        )


        if deploy_flag_answer.split(' ')[1] == '200':
            return_status = 'ON'


            check_flag_answer = do_get_request(
                target_path + 'pls',
                {
                    'p' : flag_md5
                }
            )

            if not flag in check_flag_answer:
                return_status = 'CORRUPT'

    except Exception as e:
        print(str(e))
        pass


    return return_status
