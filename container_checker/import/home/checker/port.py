#!/usr/bin/env python

import requests
import hashlib
import random
import uuid
from io import BytesIO

def check_port(tunnel_url, flag):

    return_status = 'OFF'

    try:

        flag_md5 = hashlib.md5(flag).hexdigest() + ".txt"

        deploy_flag = requests.post(
            tunnel_url + '/FileUploadServlet',
            files = {
                flag_md5: BytesIO(flag)
            }
        )

        if deploy_flag.status_code == 200:
            return_status = 'ON'

            random_check_2 = random.randrange(1,3)

            if random_check_2 == 1:

                check_lookup = requests.get(
                    tunnel_url + '/searchPortname.jsp',
                    params = {
                        'port' : 'google.com',
                    },
                    timeout = 4
                )

                if "Name:    google.com" not in check_lookup.text:
                    return_status = ('CORRUPT', '')


            check_flag = requests.get(
                     tunnel_url + "/uploads/" + flag_md5,
                     timeout = 4
            )

            if not flag in check_flag.text:
                return_status = 'CORRUPT'

    except Exception as e:
        print str(e)

    return return_status
