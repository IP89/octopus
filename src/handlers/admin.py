import tornado.ioloop
import tornado.web
import json
from helpers.db import *
from helpers.processing import *

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
       words = order_top_list(get_words())
       self.render("../templates/admin.html", title="Admin", words=words)
