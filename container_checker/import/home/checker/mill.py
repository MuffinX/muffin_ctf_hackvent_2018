#!/usr/bin/env python

import requests
import hashlib
import random
import uuid
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def check_mill(tunnel_url, flag):

    return_status = 'OFF'

    # check if online
    try:
        deploy_flag = requests.get(
            tunnel_url + 'api/values/deploy',
            params = {
                'content' : flag,
            },
            verify = False,
            timeout = 4
        )

        print(deploy_flag.status_code)

        if deploy_flag.status_code == 200:
            return_status = ('ON', '')

            #random_check_1 = random.randrange(1,3)
            #if random_check_1 == 1:
            random_check_2 = random.randrange(1,3)

            if random_check_2 == 1:
                post_gen = requests.post(
                    tunnel_url + "/api/values/send",
                    data = '<?xml version="1.0" encoding="UTF-8"?><flour>1</flour>',
                    verify = False,

                    timeout = 4
                )
                #print(post_gen.text)


                if(post_gen.text != '1'):
                    return_status = 'CORRUPT'

            elif random_check_2 == 2:
                # check send
                post_lang = requests.post(
                    tunnel_url + "/api/values/lang",
                    data = 'de.txt',
                    verify = False,

                    timeout = 4
                )
                #print(post_lang.text)

                if "Datenschutz-Richtlinie" not in post_lang.text:
                    return_status = 'CORRUPT'


                post_lang = requests.post(
                    tunnel_url + "/api/values/lang",
                    data = 'en.txt',
                    verify = False,

                    timeout = 4
                )
                #print(post_lang.text)

                if "Privacy Policy" not in post_lang.content:
                    return_status = 'CORRUPT'



            else:

                name = str(uuid.uuid4())

                check_exchange = requests.get(
                    tunnel_url + "/api/values/depositflour",
                    params = {
                        'username' : name,
                        'password' : 'default',
                        'flournr' : '69'
                    },
                    verify = False,

                    timeout = 4
                )



                post_exch = requests.post(
                    tunnel_url + "/api/values/flourstore",
                    data = name,
                    verify = False,

                    timeout = 4
                )

                if(post_exch.text != '69'):
                    return_status = 'CORRUPT'


                clean = requests.get(
                    tunnel_url + "/api/values/clean",
                    params = {
                        'name' : name
                    },
                    verify = False,

                    timeout = 4
                )

            check_flag = requests.get(
                    tunnel_url + "/api/values/getflag",
                    params = {
                        'content' : hashlib.md5(flag).hexdigest()
                    },
                    verify = False,

                    timeout = 4
                )

            if not flag in check_flag.text:
                return_status = 'CORRUPT'


    except Exception as e:
        print str(e)

    return return_status
