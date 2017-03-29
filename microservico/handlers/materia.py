# -- coding: utf-8 --

import tornado.ioloop
import tornado.web

class Materia(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('Olaa materia')



class Materias(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('OLLA MATERIAS')
