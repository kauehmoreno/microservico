# -- coding: utf-8 --
import tornado.ioloop
import tornado.web
import json
import logging
import asyncio
from helpers.db_client import DBbridge


class Integrator(tornado.web.RequestHandler):
    operations = (
        'insert',
        'bulk_insert',
        'delete',
        'bulk_delete',
        'update'
    )

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        operation = kwargs.get('operation')
        if operation is None or operation not in self.operations:
            raise tornado.web.HTTPError(404)

        db_client = DBbridge(self.application.db)

        try:
            body = json.loads(self.request.body)
        except ValueError as error:
            logging.error('Error: {}'.format(error))
            raise tornado.web.HTTPError(404)
        else:
            try:
                uuid = body.get('uuid', None)
                if uuid is None:
                    raise AttributeError()

            except AttributeError:
                raise tornado.web.HTTPError(404)
            try:
                loop = asyncio.get_event_loop()

                if operation == 'insert':
                    future = asyncio.ensure_future(db_client.insert(**body))
                if operation == 'delete':
                    pass
                if operation == 'update':
                    pass

                result = loop.run_until_complete(future)
#                loop.close()
            except Exception as e:
                logging.error('Error: {}'.format(e))
                raise tornado.web.HTTPError(500)
            else:
                self.write('Ok - 201 {}'.format(result.inserted_id))
                self.finish()



    def delete(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        raise tornado.web.HTTPError(
            405,
            'Method not allowed - please review http method use'
        )
