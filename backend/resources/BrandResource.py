from flask_restful import Resource
from flask import request
from config.mongoconnection import MongoConnection
from models.brand import Brand


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
