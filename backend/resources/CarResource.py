from flask_restful import Resource
from flask import request
from config.mongoconnection import MongoConnection
from models.car import Car
from pymongo.collection import ObjectId

from business.CarBusiness import CarBusiness


class CarResource(Resource):

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def get(self):

        carBusiness = CarBusiness()

        cars = carBusiness.findAll()

        return cars, 200

    def post(self):

        carBusiness = CarBusiness()

        car = request.json['car']
        new_car = Car(car['model'], car['brand'], car['price'], car['year'])

        car = carBusiness.saveCar(new_car)

        return car, 201


class CarFindResource(Resource):

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def get(self, id):
        carBusiness = CarBusiness()

        car_finded = carBusiness.findCarById(id)

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
