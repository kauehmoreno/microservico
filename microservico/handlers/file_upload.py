# -- coding: utf-8 --
import tornado.ioloop
import tornado.web
import json
import logging
import asyncio
from helpers.db_client import DBbridge


class Uploader(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        if not self.request.files:
            raise tornado.web.HTTPError(400)

        file1 = self.request.files['file'][0]
        original_fname = file1['filename']

        path = 'static/cover/{}'.format(original_fname)
        output_file = open(path, 'wb')
        output_file.write(file1['body'])

        self.finish("file " + original_fname + " is uploaded")

