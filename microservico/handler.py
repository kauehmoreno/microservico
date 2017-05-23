import tornado.ioloop
import tornado.web
import asyncio

def main():
    from urls import urlspatterns
    from settings import template_path
    from helpers.db_client import Client

    settings = dict(template_path=template_path)

    db = Client('materia', 'microservico')
    db = db.instance

    app = urlspatterns()
    app.db = db
    app.settings = settings
    app.listen(8888)
    app.listen(8889)
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
