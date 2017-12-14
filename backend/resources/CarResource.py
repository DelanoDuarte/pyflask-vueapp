from flask_restful import Resource
from flask import request
from config.mongoconnection import MongoConnection
from models.car import Car


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
                'year': new_car.year
            }
        )

        car_json = {
            'carId': str(result.inserted_id),
            'model': new_car.model,
            'brand': new_car.brand,
            'price': new_car.price,
            'year': new_car.year
        }

        return {'car': car_json}, 201


class CarFindResource(Resource):

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def get(self, id):
        pass
