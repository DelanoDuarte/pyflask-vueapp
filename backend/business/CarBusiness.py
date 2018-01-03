from config.mongoconnection import MongoConnection
from pymongo.collection import ObjectId


class CarBusiness:

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def saveCar(self):
        pass

    def updateCar(self, carId, car):

        car_finded = {
            'model': car['model'],
            'brand': car['brand'],
            'price': car['price'],
            'year': car['year'],
            'evaluated': car['evaluated']
        }

        self.carsDocument.update_one(
            {
                '_id': ObjectId(carId)
            },
            {
                '$set': car_finded
            }
        )

        car_updated = self.findCarById(car['_id'])

        return car_updated

    def findCarById(self, id):
        car = self.carsDocument.find_one({'_id': ObjectId(id)})
        carId = car['_id'] = str(car['_id'])

        car_finded = {
            '_id': carId,
            'model': car['model'],
            'brand': car['brand'],
            'price': car['price'],
            'year': car['year'],
            'evaluated': car['evaluated']
        }

        return car_finded
