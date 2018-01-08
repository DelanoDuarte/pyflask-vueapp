from flask_restful import Resource
from flask import request
from business.CarTypeBusiness import CarTypeBusiness

from models.cartype import CarType


class CarTypeResource(Resource):

    car_type_business = CarTypeBusiness()

    def get(self):
        return self.car_type_business.all(), 200

    def post(self):

        car_type = request.json['carType']

        car_type_saved = self.car_type_business.save(car_type)

        return car_type_saved, 201
