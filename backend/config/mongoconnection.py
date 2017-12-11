from pymongo import MongoClient


class MongoConnection:

    database_name = 'pyvueapp'
    mongoClient = MongoClient('localhost', 27017)
    mongoConnection = mongoClient[database_name]

    def getMongoConnection(self):
        connection = self.mongoConnection
        return connection
