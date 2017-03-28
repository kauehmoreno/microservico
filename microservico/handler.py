import tornado.ioloop
import tornado.web

def main():
    from urls import urlspatterns
    from settings import template_path
    from helpers.db_client import Client

    settings = dict(template_path=template_path)
    db = Client('materia')
    db = db.instance

    app = urlspatterns()
    app.db = db
    app.settings = settings
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
