import json

from flask import Flask
from flask import abort
from flask import request

namelist = [
    {
        'id': 1,
        'name': 'Tom',
        'age': 26
    },
    {
        'id': 2,
        'name': 'Dick',
        'age': 27
    },
    {
        'id': 3,
        'name': 'Harry',
        'age': 30
    }
]

app = Flask(__name__)


@app.route("/")
def index():
    return "Index page"


@app.route("/hello")
def hello():
    return "Hello, User"


@app.route("/users")
def users():
    return json.dumps(namelist)


@app.route("/user/<int:user_id>", methods=['GET'])
def user(user_id):
    result = [person for person in namelist if person['id'] == user_id]
    if len(result) == 0:
        abort(404)

    return json.dumps(result)


@app.route("/user/add", methods=['POST'])
def add_user():
    if not request.json or not ('name' and 'age' in request.json):
        abort(400)
    new_user = {
        'id': namelist[-1]['id'] + 1,
        'name': request.json['name'],
        'age': request.json['age']
    }

    namelist.append(new_user)
    return new_user, 201


@app.route("/user/delete/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    result = [person for person in namelist if person['id'] == user_id]
    if len(result) == 0:
        abort(400)
    else:
        namelist.remove(result[0])
        return {
            'result': True
        }