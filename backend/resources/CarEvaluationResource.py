from flask_restful import Resource
from flask import request
from config.mongoconnection import MongoConnection
from pymongo.collection import ObjectId
from models.carevaluation import CarEvaluation


class CarEvaluationResource(Resource):

    mongoConnection = MongoConnection()
    carEvaluationDocument = mongoConnection.mongoConnection['car-evaluation']
    carsDocument = mongoConnection.mongoConnection['cars']

    def post(self, id):

        # get the car evaluation, comming from fron-end
        car_evaluation_request = request.json['car-evaluation']

        # find the car by id and convert to string
        car = self.carsDocument.find_one({'_id': ObjectId(id)})
        carId = car['_id'] = str(car['_id'])

        # transform the car in a dictionary
        car_finded = {
            '_id': carId,
            'model': car['model'],
            'brand': car['brand'],
            'price': car['price'],
            'year': car['year'],
            'evaluated': car['evaluated']
        }

        car_finded['evaluated'] = True

        self.carsDocument.update_one(
            {
                '_id': carId
            },
            {
                '$set': car_finded
            }
        )

        car_evaluation_object = CarEvaluation(
            car_finded,
            car_evaluation_request['motor'],
            car_evaluation_request['gas'],
            car_evaluation_request['apparence'],
            car_evaluation_request['support']
        )

        result = self.carEvaluationDocument.insert_one({
            'car': car_evaluation_object.car,
            'motor': car_evaluation_object.motor,
            'gas': car_evaluation_object.gas,
            'apparence': car_evaluation_object.apparence,
            'support': car_evaluation_object.support
        })

        car_evaluation = {
            'carEvaluationId': str(result.inserted_id),
            'car': car_evaluation_object.car,
            'motor': car_evaluation_object.motor,
            'gas': car_evaluation_object.gas,
            'apparence': car_evaluation_object.apparence,
            'support': car_evaluation_object.support
        }

        return {'car-evaluation': car_evaluation}, 201
