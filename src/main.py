from tornado import ioloop, gen, web
import os.path
from handlers.form import FormHandler
from handlers.admin import AdminHandler
import tornado_mysql

application = web.Application(handlers=[
    (r"/", FormHandler),
    (r"/admin.*", AdminHandler)],
    static_path=os.path.join(os.path.dirname(__file__), "scripts"),
    template_path=os.path.join(os.path.dirname(__file__), "templates")
)

if __name__ == "__main__":

    application.listen(8888)
    ioloop.IOLoop.instance().start()
