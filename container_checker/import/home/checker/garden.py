

import requests
import hashlib
import random
import base64
import time
import sys


def check_garden(tunnel_url, flag):

    return_status = 'OFF'


    deploy_flag_yml = '''
veg:
    name: "{0}"
'''.format(flag)

    deploy_flag_yml = base64.b64encode(deploy_flag_yml)

    # check if online
    try:
        deploy_flag = requests.post(
            tunnel_url + 'add',
            data = {
                'veg' : deploy_flag_yml
            },
            timeout = 4
        )


        if deploy_flag.status_code == 200:
            return_status = 'ON'

            time.sleep(1)

            check_flag = requests.get(
                tunnel_url + 'get',
                params = {
                    'hash' : hashlib.md5(flag).hexdigest()
                },
                timeout = 4
            )

            if not flag in check_flag.text:
                return_status = 'CORRUPT'


    except Exception as e:
        sys.stderr.write(str(e))
        print str(e)


    return return_status
