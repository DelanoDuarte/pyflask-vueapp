from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from HomeResource import HomeResource, TestHomeResource
from resources.CarResource import CarResource
from resources.BrandResource import BrandResource


app = Flask(__name__)
api = Api(app, prefix='/py-vue/api')
CORS(app)

api.add_resource(HomeResource, '/')
api.add_resource(TestHomeResource, '/test')

#Car Resources
api.add_resource(CarResource, '/cars')

#Brand Resources
api.add_resource(BrandResource, '/brands')

app.run(debug=True, port=5000)
