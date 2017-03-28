# -- coding: utf-8 --

import tornado.ioloop
import tornado.web

class Materia(tornado.web.RequestHandler):

    def get(self):
        self.write('Olaa materia')

