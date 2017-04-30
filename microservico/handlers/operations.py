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
        'delete',
        'update'
    )

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        operation = kwargs.get('operation')
        if operation is None or operation not in self.operations:
            raise tornado.web.HTTPError(404)

        db_client = DBbridge(self.application.db)

        try:
            body = json.loads(self.request.body.decode('utf-8'))
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
            else:

                loop = asyncio.get_event_loop()
                try:

                    if operation == 'insert':
                        future = asyncio.ensure_future(db_client.insert(**body))
                    if operation == 'delete':
                        future = asyncio.ensure_future(db_client.delete(uuid))
                    if operation == 'update':
                        future = asyncio.ensure_future(db_client.update(**body))

                    result = loop.run_until_complete(future)
#                loop.close()
                except Exception as e:
                    logging.error('Error: {}'.format(e))
                    raise tornado.web.HTTPError(500)
                else:
                    try:
                        self.write('Ok - 201 {}'.format(result.inserted_id))
                    except AttributeError:
                        self.write('OK - 204 {}'.format(result.raw_result))
                    self.finish()


    def delete(self, *args, **kwargs):
        raise tornado.web.HTTPError(
            405,
            'Method not allowed - please review http method use'
        )

    def put(self, *args, **kwargs):
        raise tornado.web.HTTPError(
            405,
            'Method not allowed - please review http method use'
        )
