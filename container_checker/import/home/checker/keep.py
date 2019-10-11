#!/usr/bin/env python

import requests
import hashlib
import random
import uuid

def check_keep(tunnel_url, flag):

    return_status = 'OFF'

    # check if online
    try:
        deploy_flag = requests.get(
            tunnel_url + 'inc/ser.php',
            params = {
                'invite' : flag,
            },
            timeout = 4
        )


        if deploy_flag.status_code == 200:
            return_status = 'ON'


            random_check_2 = random.randrange(1,3)

            if random_check_2 == 1:
                username = "a" + str(uuid.uuid4()).replace("-","X")
                password = "a" + str(uuid.uuid4()).replace("-","X")

                post_gen = requests.Session()

                post_gen.post(
                    tunnel_url + "inc/register.php",
                    data = {
                        'username': username,
                        'password': password
                    },
                    verify = False,

                    timeout = 4
                )

                res = post_gen.post(
                    tunnel_url + "inc/login.php",
                    data = {
                        'username': username,
                        'password': password
                    },
                    verify = False,

                    timeout = 4
                )

                if "Your Username is: " + username not in res.text:
                    return_status = 'CORRUPT'


            elif random_check_2 == 2:
                post_gen = requests.post(
                    tunnel_url + "inc/dinner.php",
                    params = 'r=a:2:{i:0;s:4:"TEST";i:1;s:5:"FOODS";}',
                    verify = False,

                    timeout = 4
                )
                if "Thanks for submitting dinner reservation: TEST - FOODS" not in post_gen.text:
                    return_status = 'CORRUPT'


            elif random_check_2 == 3:
                post_gen = requests.post(
                    tunnel_url + "inc/userinfo.php",
                    data = {
                        "name" : "secret.txt"
                    },
                    verify = False,

                    timeout = 4
                )
                if "Hidden stuffz like this" not in post_gen.text:
                    return_status = 'CORRUPT'


            check_flag = requests.get(
                    tunnel_url + "invitation/" + hashlib.md5(flag).hexdigest(),
                    verify = False,
                    timeout = 4
                )

            if not flag in check_flag.text:
                return_status = 'CORRUPT'


    except Exception as e:
        print 'keep checker: ' + str(e)

    return return_status
