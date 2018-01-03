from config.mongoconnection import MongoConnection
from models.carevaluation import CarEvaluation
from pymongo.collection import ObjectId

from business.CarBusiness import CarBusiness


class CarEvaluationBusiness:

    mongoConnection = MongoConnection()
    carEvaluationDocument = mongoConnection.mongoConnection['car-evaluation']
    carsDocument = mongoConnection.mongoConnection['cars']

    def save(self, car_evaluation, carId, car):

        carBusiness = CarBusiness()

        car['evaluated'] = True
        updated_car = carBusiness.updateCar(carId, car)

        result = self.carEvaluationDocument.insert_one({
            'car': updated_car,
            'motor': car_evaluation.motor,
            'gas': car_evaluation.gas,
            'apparence': car_evaluation.apparence,
            'support': car_evaluation.support
        })

        car_evaluation_saved = self.findById(result.inserted_id)

        return car_evaluation_saved

    def findById(self, id):
        car_evaluation = self.carEvaluationDocument.find_one(
            {'_id': ObjectId(id)})
        car_evaluationId = car_evaluation['_id'] = str(car_evaluation['_id'])

        car_evaluation_finded = {
            '_id': car_evaluationId,
            'car': car_evaluation['car'],
            'motor': car_evaluation['motor'],
            'gas': car_evaluation['gas'],
            'apparence': car_evaluation['apparence'],
            'support': car_evaluation['support']
        }

        return car_evaluation_finded
