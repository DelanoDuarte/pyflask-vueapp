from config.mongoconnection import MongoConnection
from pymongo.collection import ObjectId


class CarBusiness:

    mongoConnection = MongoConnection()
    carsDocument = mongoConnection.mongoConnection['cars']

    def findAll(self):
        cars = self.carsDocument.find({})
        carsJson = []

        for car in cars:
            car['_id'] = str(car['_id'])
            carsJson.append(car)

        car_list = {
            'cars': carsJson
        }

        return car_list

    def saveCar(self, car):

        result = self.carsDocument.insert_one(
            {
                'model': car.model,
                'brand': car.brand,
                'price': car.price,
                'year': car.year,
                'car_type': car.car_type,
                'evaluated': False
            }
        )

        car_saved = {
            'carId': str(result.inserted_id),
            'model': car.model,
            'brand': car.brand,
            'price': car.price,
            'year': car.year,
            'car_type': car.car_type,
            'evaluated': car.evaluated
        }

        return car_saved

    def updateCar(self, carId, car):

        car_finded = {
            'model': car['model'],
            'brand': car['brand'],
            'price': car['price'],
            'year': car['year'],
            'car_type': car['car_type'],
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
            'car_type': car['car_type'],
            'evaluated': car['evaluated']
        }

        return car_finded

    def deleteCar(self, id):
        self.carsDocument.delete_one({'_id': ObjectId(id)})
