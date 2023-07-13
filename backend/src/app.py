from flask import Flask, request, make_response, jsonify
import os
from sqlalchemy.orm import Session
from models import User, connect_db
backend_port = os.environ.get('BACKEND_PORT', '8888')

postgres_host = os.environ.get('POSTGRES_HOST', 'localhost')
postgres_port = os.environ.get('POSTGRES_PORT', '5432')

postgres_user = os.environ.get('POSTGRES_USER', 'postgres')
postgres_password = os.environ.get('POSTGRES_PASSWORD', 'postgres')
postgres_db = os.environ.get('POSTGRES_DB', 'postgres')

app = Flask(__name__)

engine = connect_db(postgres_user, postgres_password,
                    postgres_host, postgres_port, postgres_db)


@app.route('/')
def index():
    with Session(engine) as session:
        users = session.query(User).all()
    return jsonify([user.to_dict() for user in users])


@app.route('/add', methods=['POST'])
def add():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')

    with Session(engine) as session:
        user = User(first_name=first_name, last_name=last_name)
        session.add(user)
        session.commit()

    return make_response("Ok", 200)


@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    with Session(engine) as session:
        user = session.query(User).filter(User.id == id).first()
        session.delete(user)
        session.commit()

    return make_response("Ok", 200)


@app.route('/<int:id>', methods=['PUT'])
def update(id):
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')

    with Session(engine) as session:
        user = session.query(User).filter(User.id == id).first()
        user.first_name = first_name
        user.last_name = last_name
        session.commit()

    return make_response("Ok", 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=backend_port)
