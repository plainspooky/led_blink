#!/usr/bin/env python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 softtabstop=4

import json
from bottle import error, route, run, static_file, template
from api import v1

__author__ = 'Giovanni Nunes'
__version__ = '1'

# led=mraa.Gpio(13)

@route('/')
def index():
    '''
        página principal e página de controle dos leds
    '''
    return template('template/index.tpl')

@route('/static/<fname:path>')
def static(fname):
    '''
        fornece os arquivos estáticos utilizados pela aplicação
    '''
    return static_file(fname, root='static')

@error(404)
def error404(error):
    '''
        página para o erro 404 -- outras seriam implementadas do mesmo modo
    '''
    return template('template/404.tpl')

run(host='0.0.0.0', port=8080, debug=True)
