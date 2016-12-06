#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json
from bottle import get, put, request, response, route
import mraa

''' abstrai a estrutura dos leds no Edison '''
leds={
        '1' : mraa.Gpio(13) 
    }

@get('/led/<led>')
def get_once(led):
    if led in leds:
        ''' se o "led" informado existe no dicionário "leds"... '''
        value=leds[led].read()
    else:
        ''' senão retorna false como valor do led '''
        value=False
    response.status=200
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({ 'value': value })

@put('/led/<led>/<value>')
def set_value(led,value):
    success=False
    if led in leds:
        ''' bem simples, '1' acende e '0' apaga, ignora-se o resto '''
        if value=='1':
            ''' se o valor for "1" eu acendo o led '''
            leds[led].dir(mraa.DIR_OUT)
            leds[led].write(1)
            success=True
        elif value=='0':
            ''' e se o valor for "0" eu o apago '''
            leds[led].dir(mraa.DIR_OUT)
            leds[led].write(0)
            success=True
    ''' independente dos valores de "led" ou "valor" chega-se aqui, daí é 200 '''
    response.status=200
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({ 'success': success })
