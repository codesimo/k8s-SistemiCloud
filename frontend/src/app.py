from flask import Flask, render_template, request, redirect, url_for, flash, session, Response, make_response
import os
import requests

app = Flask(__name__)
port = int(os.environ.get("FRONTEND_PORT", 5000))

backend_host = os.environ.get('BACKEND_HOST', 'backend')
backend_port = os.environ.get('BACKEND_PORT', '8888')


@app.route('/')
def index():
    elements = [{"id": 1, "first_name": "Simo", "last_name": "B"}]
    try:
        elements = requests.get(
            f'http://{backend_host}:{backend_port}/').json()
    except Exception as e:
        return make_response('Non funziona il backend! ' + str(e), 500)
    return render_template('index.html', elements=elements)


@app.route('/add', methods=['POST'])
def add():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    try:
        requests.post('http://backend:8888/add',
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
