from flask_restful import Resource
from flask import request


class HomeResource(Resource):

    def get(self):
        hello = 'App Running !'
        return {'data': hello}


class TestHomeResource(Resource):

    names = []

    def get(self):
        data = []
        for name in self.names:
            data.append(name)

        json = {'data': data}
        return json

    def post(self):
        data = request.get_json()
        new_name = {'name': data['name']}
        self.names.append(new_name)
        json = {'data': new_name}
        return json
