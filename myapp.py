import json
import requests

URL = 'http://127.0.0.1:8000/student/'


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# get_data(2)


def post_data():
    data = {
        'name': 'Ishaan',
        'roll': 104,
        'city': 'Tahiti'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# post_data()
# get_data()


def put_data(id):
    data = {
        'id': id,
        'name': 'Aisha',
        'roll': 104,
        'city': 'Malaysia'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# put_data(2)
# get_data()


def patch_data(id):
    data = {
        'id': id,
        'name': 'Zaisha',
        'roll': 105,
    }
    json_data = json.dumps(data)
    r = requests.patch(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# patch_data(5)
# get_data()


def delete_data(id):
    data = {'id': id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# delete_data(2)
# get_data()
