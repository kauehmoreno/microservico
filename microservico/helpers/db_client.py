# coding:utf-8
import logging
import motor
import json
from tornado.ioloop import IOLoop

class Client(object):

    def __init__(self, database_name):
        self.database_name = database_name
        self.__client = motor.motor_tornado.MotorClient(
            'localhost', 27017
        )
        self.__create_database()

    @property
    def instance(self):
        materia = self.database_name
        return self.__client.materia

    def __create_database(self):
        self.__client[self.database_name]



class DBbridge(object):
    def __init__(self, client=None):
        if client is None:
            raise AttributeError(
                'É necessário inserir a instancia do banco disponível '
                'no self.db para que seja executado as querys no mongo '
                'reaproveitando instancia para que nao seja aberto uma '
                'a cada request '
            )
        self.client = client

    @classmethod
    async def insert(cls, **kwargs):
        await self.client.test_collection.insert_one(kwargs)


    @classmethod
    async def bulk_insert(cls, bulk):
        def insert(item):
            await self.client.test_collection.insert_one(item)
        map(insert, bulk)


    @classmethod
    async def filter(self, limit=None, order_by=None):
        if limit is None:
            limit = 20

        if order_by is None:
            order_by = -1
        else:
            order_by = order_by

        return await self.client.test_collection.find().sort({'data_publicacao': order_by}).limit(limit)


    @classmethod
    async def get(self, uuid):
        try:
            return await self.client.test_collection.find_one({'uuid': uuid})
        except Exception as e:
            msg = 'Não foi possível pegar o documento. id: {} error: {}'
            loggin.error(msg.format(uuid, e))
            return {}


    @classmethod
    async def update(self, **kwargs):
        uuid = _dict.get('uuid', '')
        if uuid:
            await self.client.test_collection.replace_one({'uuid': uuid}, kwargs)


    @classmethod
    async def delete(self, uuid):
        await db.test_collection.delete_one({'uuid': uuid})


    @classmethod
    async def bulk_delete(self, bulk):
        def delete(uuid):
            await db.test_collection.delete_one({'uuid': uuid})

        map(delete, bulk)
