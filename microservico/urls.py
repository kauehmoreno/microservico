# -- coding: utf-8 --
import tornado.web
from handlers.main_page import MainHandler
from handlers.materia import Materia, Materias
from handlers.operations import Integrator
from settings import static_path

def urlspatterns():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/materia/(?P<_id>[\w]+)/$', Materia),
        (r'/materias/(?P<order_by>[\w]+)/(?P<limit>[\d+]+)/$', Materias),
        (r'/api/v1/(?P<operation>[\w]+)/?$', Integrator),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path})
    ])


