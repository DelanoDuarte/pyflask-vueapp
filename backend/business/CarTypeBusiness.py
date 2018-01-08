from config.mongoconnection import MongoConnection
from pymongo.collection import ObjectId


class CarTypeBusiness:

    mongoConnection = MongoConnection()
    carTypeDocument = mongoConnection.mongoConnection['car-type']

    def save(self, cartype):

        car_type_id = self.carTypeDocument.insert_one({
            'name': cartype['name']
        })

        car_type_saved = {
            '_id': str(car_type_id.inserted_id),
            'name': cartype['name']
        }

        return car_type_saved

    def all(self):

        car_type_list = []
        car_type_cursor = self.carTypeDocument.find({})

        for car_type in car_type_cursor:
            car_type['_id'] = str(car_type['_id'])
            car_type_list.append(car_type)

        car_types_json = {
            'data': car_type_list
        }

        return car_types_json
