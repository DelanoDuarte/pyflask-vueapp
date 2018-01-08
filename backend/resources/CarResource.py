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
        new_car = Car(car['model'], car['brand'],
                      car['price'], car['year'], car['car_type'])

        car = carBusiness.saveCar(new_car)

        return car, 201


class CarFindResource(Resource):

    carBusiness = CarBusiness()

    def get(self, id):
        car_finded = self.carBusiness.findCarById(id)

        return car_finded, 200

    def put(self, id):

        car_request = request.json['car']

        car_update = {
            'model': car_request['model'],
            'brand': car_request['brand'],
            'price': car_request['price'],
            'year': car_request['year'],
            'car_type': car_request['car_type']
        }

        car_updated = self.carBusiness.updateCar(id, car_update)

        return {'car': car_updated}, 200

    def delete(self, id):

        car_finded = self.carBusiness.deleteCar(id)
        return {'Brand': 'Brand Deleted'}, 200
