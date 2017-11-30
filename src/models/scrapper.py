from bs4 import BeautifulSoup
from helpers.processing import *
import urllib2

class Scrapper:
    def __init__(self, url):
        self.url = url

    def get_works_list(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulSoup(page, 'html.parser')
        texts_array = filter(tag_visible, soup.findAll(text=True))
        words_array = get_words_array(texts_array)
        return self.array_to_list(words_array)


    def array_to_list(self, words):
        result = {}

        for word in words:
            word = word.lower()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

        return result
