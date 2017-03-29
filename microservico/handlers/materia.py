# -- coding: utf-8 --
import logging
import tornado.ioloop
import tornado.web
import json
import asyncio
from helpers.db_client import DBbridge

class Materia(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        uuid = kwargs.get('_id')

        db_client = DBbridge(self.application.db)

        try:
            loop = asyncio.get_event_loop()
            future = asyncio.ensure_future(db_client.get(uuid))
            result = loop.run_until_complete(future)
        except Exception as e:
            self.write(json.dumps({'error': e}))
            self.finish()

        else:
            if result:
                result.pop('_id')
                self.set_header("Content-Type", "application/json; charset=UTF-8")
                self.write(json.dumps(result))
            else:
                self.write(json.dumps({}))

        self.finish()


class Materias(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        DEFAULT_LIMIT = 20

        order = {'esc': 1, 'desc': -1}
        order_by = order.get(kwargs.get('order_by'))
        limit = kwargs.get('limit')

        db_client = DBbridge(self.application.db)

        if not order_by:
            order_by = -1

        if int(limit) < 1:
            limit = 20


        loop = asyncio.get_event_loop()
        try:
            future = asyncio.ensure_future(db_client.filter(limit=int(limit), order_by=order_by))
            result = loop.run_until_complete(future)
        except Exception as e:
            self.write(json.dumps({'error': str(e)}))
            self.finish()
        else:
            if not result:
                result = {}

            self.set_header("Content-Type", "application/json; charset=UTF-8")

            self.write(json.dumps(result))
            self.finish()

