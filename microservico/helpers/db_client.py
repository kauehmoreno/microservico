# coding:utf-8
import logging
import motor
import json
from tornado.ioloop import IOLoop
from tornado import gen
import motor.motor_asyncio


class Client(object):

    def __init__(self, database_name, collection_name):
        self.database_name = database_name
        self.collection_name = collection_name
        self.__client = motor.motor_asyncio.AsyncIOMotorClient(
            'localhost', 27017
        )
        self.__db = self.__create_database()
        self.__collection = self.__create_collection()


    @property
    def instance(self):
        materia = self.database_name
        return self.__collection

    def __create_database(self):
        db = self.__client[self.database_name]
        return db

    def __create_collection(self):
        collection = self.__db[self.collection_name]
        return collection



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

    async def insert(self, **kwargs):
        result =  await self.client.test_collection.insert_one(kwargs)
        return result

    async def filter(self, limit=None, order_by=None):
        if limit is None:
            limit = 20

        if order_by is None:
            order_by = -1
        else:
            order_by = order_by

        cursor = self.client.test_collection.find().sort('data_publicacao', order_by).limit(limit)
        result = []
        for document in await cursor.to_list(length=100):
            document.pop('_id')
            result.append(document)

        return result


    async def get(self, uuid):
        try:
            return await self.client.test_collection.find_one({'uuid': uuid})
        except Exception as e:
            msg = 'Não foi possível pegar o documento. id: {} error: {}'
            loggin.error(msg.format(uuid, e))
            return {}


    async def update(self, **kwargs):
        uuid = _dict.get('uuid', '')
        if uuid:
            await self.client.test_collection.replace_one({'uuid': uuid}, kwargs)


    async def delete(self, uuid):
        await db.test_collection.delete_one({'uuid': uuid})
