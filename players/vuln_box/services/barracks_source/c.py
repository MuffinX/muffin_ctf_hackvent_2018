import os
import sys
import ctypes
import base64
from flask import Flask, request, render_template
from easyprocess import EasyProcess
from werkzeug.serving import run_simple

#begin_multiline
def _yes(): return 'yes'
#end_multiline
