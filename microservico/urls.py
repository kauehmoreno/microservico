# -- coding: utf-8 --
import tornado.web
from handlers.main_page import MainHandler
from handlers.materia import Materia


def urlspatterns():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/materia/', Materia)
    ])


