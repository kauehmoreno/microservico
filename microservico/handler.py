import tornado.ioloop
import tornado.web

def main():
    from urls import urlspatterns
    from settings import template_path
    settings = dict(template_path=template_path)
    app = urlspatterns()
    app.settings = settings
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
