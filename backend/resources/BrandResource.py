from flask_restful import Resource
from flask import request
from config.mongoconnection import MongoConnection
from models.brand import Brand
from pymongo.collection import ObjectId


class BrandResource(Resource):

    mongoConnection = MongoConnection()
    brandDocument = mongoConnection.mongoConnection['brands']

    def get(self):
        brands = self.brandDocument.find({})
        brandsJson = []

        for brand in brands:
            brand['_id'] = str(brand['_id'])
            brandsJson.append(brand)

        return {'data': brandsJson}

    def post(self):

        brandJson = request.json['brand']
        print(brandJson)

        brand = Brand(brandJson['name'], brandJson['active'])

        new_brand = {
            'name': brand.name,
            'active': brand.active
        }

        self.brandDocument.insert_one({
            'name': brand.name,
            'active': brand.active
        })

        return new_brand, 201


class FindOneBrandResource(Resource):

    mongoConnection = MongoConnection()
    brandDocument = mongoConnection.mongoConnection['brands']

    def get(self, id):
        brand = self.brandDocument.find_one({'_id': ObjectId(id)})

        brand_finded = {
            'name': brand['name'],
            'active': brand['active']
        }

        return {'brand': brand_finded}

    def put(self, id):

        brandJson = request.json['brand']

        brand_update = {
            'name': brandJson['name'],
            'active': brandJson['active']
        }

        brand = self.brandDocument.update_one(
            {'_id': ObjectId(id)}, {'$set': brand_update})

        return {'brand': brand_update}
