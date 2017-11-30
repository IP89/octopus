import tornado.ioloop
import tornado.web
import json
from models.scrapper import Scrapper
from helpers.processing import *
from helpers.db import *


class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../templates/cloud.html", title="Cloud")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        url = self.get_argument("url")
        scrapper = Scrapper(url);
        w_list = scrapper.get_works_list();
        top_words_ordered = order_top_list(w_list)

        set_new_words(top_words_ordered)

        self.write(json.dumps(top_words_ordered))