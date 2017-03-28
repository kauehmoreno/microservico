# coding:utf-8
import motor

class Client(object):

    def __init__(self, database_name):
        self.database_name = database_name
        self.__client = motor.motor_tornado.MotorClient(
            'localhost', 27017
        )
        self.__create_database()

    @property
    def instance(self):
        return self.__client.database_name

    def __create_database(self):
        self.__client[self.database_name]

