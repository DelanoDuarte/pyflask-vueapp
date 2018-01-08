from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from HomeResource import HomeResource, TestHomeResource
from resources.CarResource import CarResource, CarFindResource
from resources.BrandResource import BrandResource, FindOneBrandResource
from resources.CarEvaluationResource import CarEvaluationResource
from resources.CarTypeResource import CarTypeResource


app = Flask(__name__)
api = Api(app, prefix='/py-vue/api')
CORS(app)

api.add_resource(HomeResource, '/')
api.add_resource(TestHomeResource, '/test')

# Car Resources
api.add_resource(CarResource, '/cars')
api.add_resource(CarFindResource, '/cars/<string:id>')

# Brand Resources
api.add_resource(BrandResource, '/brands')
api.add_resource(FindOneBrandResource, '/brands/<string:id>')

# Car Evaluation Resources
api.add_resource(CarEvaluationResource, '/car-evaluation/<string:id>')


# Car Type Resources
api.add_resource(CarTypeResource, '/car-type')

app.run(debug=True, port=5000)
