from flask import Flask, render_template, request, redirect, url_for, flash, session, Response, make_response
import os
import requests
import socket

hostname = socket.gethostname()
app = Flask(__name__)
port = int(os.environ.get("FRONTEND_PORT", '5000'))

backend_host = os.environ.get('BACKEND_HOST', 'backend')
backend_port = int(os.environ.get('BACKEND_PORT', '8888'))


@app.route('/')
def index():
    elements = [{"id": 1, "first_name": "Simo", "last_name": "B"}]
    try:
        elements = requests.get(
            f'http://{backend_host}:{backend_port}/').json()
        backend_name = requests.get(
            f'http://{backend_host}:{backend_port}/name').text
    except Exception as e:
        return make_response('Non funziona il backend! ' + str(e), 500)
    return render_template('index.html', elements=elements, frontend_name=hostname, backend_name=backend_name)


@app.route('/add', methods=['POST'])
def add():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    try:
        requests.post(f'http://{backend_host}:{backend_port}/add',
                      json={"first_name": first_name, "last_name": last_name})
    except Exception as e:
        return make_response('Non funziona il backend! ' + str(e), 500)

    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    try:
        requests.delete(f'http://{backend_host}:{backend_port}/{id}')
    except Exception as e:
        return make_response('Non funziona il backend! ' + str(e), 500)

    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    try:
        requests.put(f'http://{backend_host}:{backend_port}/{id}',
                     json={"first_name": first_name, "last_name": last_name})
    except Exception as e:
        return make_response('Non funziona il backend! ' + str(e), 500)

    return redirect(url_for('index'))


@app.route('/health')
def health():
    return make_response('Ok', 200)


@app.route('/die')
def die():
    os._exit(1)


@app.route('/kill-backend')
def kill_backend():
    requests.get(f'http://{backend_host}:{backend_port}/die')
    return make_response('Ok', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
