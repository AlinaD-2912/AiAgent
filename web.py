from bottle import Bottle
from bottle import Bottle, template
from bottle import request
from bottle import Bottle, static_file, template

from bottle import redirect

app = Bottle()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@app.route('/')
def index():
    return template('index')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, reloader=True)

