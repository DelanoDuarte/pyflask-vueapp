from flask_restful import Resource
from flask import request
from models.carevaluation import CarEvaluation

from business.CarBusiness import CarBusiness
from business.CarEvaluationBusiness import CarEvaluationBusiness


class CarEvaluationResource(Resource):

    carBusiness = CarBusiness()
    carEvaluationBusiness = CarEvaluationBusiness()

    def post(self, id):

        # get the car evaluation, comming from fron-end
        car_evaluation_request = request.json['car-evaluation']

        # find the car by id and convert to string
        car = self.carBusiness.findCarById(id)

        # creates a new car_evaluation object
        car_evaluation_object = CarEvaluation(
            car,
            car_evaluation_request['motor'],
            car_evaluation_request['gas'],
            car_evaluation_request['apparence'],
            car_evaluation_request['support']
        )

        # send params to business to make business rule necessary
        car_evaluation = self.carEvaluationBusiness.save(
            car_evaluation_object, car['_id'], car)

        return {'car-evaluation': car_evaluation}, 201


class CarEvaluationFindOneResource(Resource):

    carBusiness = CarBusiness()
    carEvaluationBusiness = CarEvaluationBusiness()

    def get(self, id):
        car_evaluation = self.carEvaluationBusiness.findById(id)

        return car_evaluation, 200


class CarEvaluationFindByCar(Resource):

    carBusiness = CarBusiness()
    carEvaluationBusiness = CarEvaluationBusiness()

    def get(self, id):
        car_evaluation = self.carEvaluationBusiness.findByCarId(id)

        return car_evaluation, 200
