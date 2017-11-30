import urllib2
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import OrderedDict


PREPOSITIONS = ["with", "at", "from", "into", "during", "including", "until",
    "against", "among", "throughout", "despite", "towards", "upon", "concerning", "to",
    "in", "for", "on", "by", "about", "like", "through", "over", "before", "between", "after", "since",
    "without", "under", "within", "along", "following", "across", "behind", "beyond",  "plus", "except",
    "but", "up", "out", "around", "down", "off", "above", "near", "of"]

ARTICLES = ["the", "a", "one", "some", "few"]

def order_top_list(words):
    sorted_list = OrderedDict()
    pairs = sorted(words.items(), key=lambda kv: kv[1], reverse=True)
    counter = 0
    for pair in pairs:
        if counter == 100: break
        if pair[0] in PREPOSITIONS or pair[0] in ARTICLES: continue

        sorted_list[pair[0]] = pair[1]
        counter += 1

    return sorted_list

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def get_words_array(texts):
    result = []
    for text in texts:
        result += get_words_on_text(text)

    return result

def get_words_on_text(text):
    words = text.split(" ")
    result = []

    for word in words:
        word = filter(lambda x: x.isalpha(), word)
        if len(word) > 0:
            result.append(word)

    return result


