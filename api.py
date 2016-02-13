#!/usr/bin/env python
import json
from bottle import hook, route, run, request

from yomuu import preprocess
from yomuu import preprocess

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@route('/')
def index():
    print('hello')

@route('/textFeature', 'GET')
def get_text_feature():
    text = preprocess.normalize(request.query.decode().get('text'))
    result = preprocess.extract_text_feature(text)

    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
