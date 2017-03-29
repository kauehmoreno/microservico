# -- coding: utf-8 --
import tornado.web
from handlers.main_page import MainHandler
from handlers.materia import Materia
from handlers.operations import Integrator


def urlspatterns():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/materia/', Materia),
        (r'/api/v1/(?P<operation>[\w]+)/?$', Integrator)
    ])


