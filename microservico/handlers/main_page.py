# -- coding: utf-8 --

import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        items = ['lala', 'kadu']
        self.render('home.html', title='Ola', items=items)
