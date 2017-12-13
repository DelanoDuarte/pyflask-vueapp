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

        model = request.json['model']
        brand = request.json['brand']
        price = request.json['price']
        year = request.json['year']

        car = Car(model, brand, price, year)

        new_car = {
            'model': car.model,
            'brand': car.brand,
            'price': car.price,
            'year': car.year
        }

        self.carsDocument.insert_one(
            {
                'model': car.model,
                'brand': car.brand,
                'price': car.price,
                'year': car.year
            }
        )

        return new_car, 201


class CarFindResource(Resource):

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def get(self, id):
        pass
