#!/usr/bin/env python

import base64
import hashlib
import random
import os
import string

def get_random_variable_name(len):
    return ''.join(random.choice(string.ascii_letters) for i in range(len))

def obsfucate_code(plain_code):

    obsfucated_code = ''
    multiline_activated = False
    multiline_code = ''


    exec_rnd_name = get_random_variable_name(10)
    obsfucated_code += '{0}=exec;'.format(exec_rnd_name)

    base64_rnd_name = get_random_variable_name(10)
    obsfucated_code += '{0}=base64.b64decode;'.format(base64_rnd_name)

    for plain_line in plain_code.split('\n'):
        if len(plain_line) == 0: continue

        if '#begin_multiline' in plain_line:
            multiline_activated = True
            multiline_code = ''
        if '#end_multiline' in plain_line:
            multiline_activated = False
            obsfucated_code += "{0}({1});".format(exec_rnd_name, multiline_code)
            multiline_code = ''
        else:
            b64_payload = base64.b64encode(plain_line +('\n' if multiline_activated else ''))

            if multiline_activated:
                multiline_code += ('+' if len(multiline_code) > 0 else '') + "{0}('{1}')".format(base64_rnd_name, b64_payload)
            else:
                obs_line = "{0}({1}('{2}'));".format(exec_rnd_name, base64_rnd_name, b64_payload)
                obsfucated_code += obs_line


    return obsfucated_code

def obsfucate_file(input_file, output_file):

    plain_code = ''
    with open(input_file, 'r') as read_plain: plain_code = read_plain.read()

    obsfucated_file_code = '#!/usr/bin/env python3\n# muffinx_obsfucator\nimport base64;'

    obsfucated_code = plain_code

    for i in range(10):
        obsfucated_code = obsfucate_code(obsfucated_code)

    obsfucated_file_code += obsfucated_code

    with open(output_file, 'w') as write_obsfucated: write_obsfucated.write(obsfucated_file_code)


obsfucate_file('a.py', '../barracks/a.py')
obsfucate_file('b.py', '../barracks/b.py')
obsfucate_file('c.py', '../barracks/c.py')
obsfucate_file('d.py', '../barracks/d.py')
obsfucate_file('e.py', '../barracks/e.py')
obsfucate_file('main.py', '../barracks/main.py')
