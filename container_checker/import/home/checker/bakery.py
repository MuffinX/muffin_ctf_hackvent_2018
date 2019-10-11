

import requests
import hashlib
import random


def check_bakery(tunnel_url, flag):

    return_status = 'OFF'

    # check if online
    try:
        deploy_flag = requests.get(
            tunnel_url + 'inc/inc.php',
            params = {
                'page' : 'breads.php',
                'bread' : flag
            },
            timeout = 4
        )


        if deploy_flag.status_code == 200:
            return_status = 'ON'

            #random_check_1 = random.randrange(1,3)
            #if random_check_1 == 1:
            random_check_2 = random.randrange(1,3)

            if random_check_2 == 1:
                # check calc
                n_1 = random.randrange(2,200)
                n_2 = random.randrange(2,200)

                calc_res = str('{0:.2f}'.format(((n_1 + n_2) * 1.20)))


                check_calc = requests.get(
                    tunnel_url + 'inc/inc.php',
                    params = {
                        'page' : 'breads.php',
                        'prize' : '( ' + str(n_1) + ' + ' + str(n_2) + ')'
                    },
                    timeout = 4
                )

                if not calc_res in check_calc.text:
                    return_status = 'CORRUPT'

            else:
                # check send
                check_send = requests.get(
                    tunnel_url + 'inc/inc.php',
                    params = {
                        'page' : 'breadSend.php',
                        'ip' : '0.0.0.0'
                    },
                    timeout = 4
                )

                if 'PING 0.0.0.0 (127.0.0.1) 56(84) bytes of data.' not in check_send.text:
                    return_status = 'CORRUPT'

            check_flag = requests.get(
                tunnel_url + 'breads/' + hashlib.md5(flag).hexdigest(),
                timeout = 4
            )

            if not flag in check_flag.text:
                return_status = 'CORRUPT'
    except Exception as e:
        print str(e)

    return return_status
