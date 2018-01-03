from flask_restful import Resource
from flask import request
from config.mongoconnection import MongoConnection
from models.car import Car
from pymongo.collection import ObjectId


class CarResource(Resource):

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def get(self):
        cars = self.carsDocument.find({})
        carsJson = []

        for car in cars:
            car['_id'] = str(car['_id'])
            carsJson.append(car)

        return {'cars': carsJson}

    def post(self):
        car = request.json['car']
        new_car = Car(car['model'], car['brand'], car['price'], car['year'])

        result = self.carsDocument.insert_one(
            {
                'model': new_car.model,
                'brand': new_car.brand,
                'price': new_car.price,
                'year': new_car.year,
                'evaluated': False
            }
        )

        car_json = {
            'carId': str(result.inserted_id),
            'model': new_car.model,
            'brand': new_car.brand,
            'price': new_car.price,
            'year': new_car.year,
            'evaluated': new_car.evaluated
        }

        return {'car': car_json}, 201


class CarFindResource(Resource):

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def get(self, id):
        car = self.carsDocument.find_one({'_id': ObjectId(id)})
        carId = car['_id'] = str(car['_id'])

        car_finded = {
            'carId': carId,
            'model': car['model'],
            'brand': car['brand'],
            'price': car['price'],
            'year': car['year']
        }

        return car_finded, 200

    def put(self, id):

        car_request = request.json['car']

        car_update = {
            'model': car_request['model'],
            'brand': car_request['brand'],
            'price': car_request['price'],
            'year': car_request['year']
        }

        self.carsDocument.update_one(
            {
                '_id': ObjectId(id)
            },
            {
                '$set': car_update
            }
        )

        return {'car': car_update}, 200

    def delete(self, id):
        car_delete = self.carsDocument.delete_one({'_id': ObjectId(id)})
        return {'Brand': 'Brand Deleted'}, 200
