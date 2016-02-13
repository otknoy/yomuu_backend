#!/usr/bin/env python
import json
from bottle import route, run, request

from yomuu import preprocess
from yomuu import preprocess

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
