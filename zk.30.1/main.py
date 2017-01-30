"""
Ranking jmen na strance, Zkouska 30.1.
"""
import json
import re
import urllib
from urllib.request import urlopen
from html.parser import HTMLParser


class Word:
    """ Slovo na strance """

    def __init__(self, word, index):
        """konstruktor"""
        self.word = word
        self.index = index
        self.rank = 0
        for ch in word:
            self.rank += ord(ch) - 64
        self.rank *= index

    def get_rank(self):
        """vrati ranking"""
        return self.rank

    def get_word(self):
        """vrati slovo"""
        return self.word


class Stripper(HTMLParser):
    """ Odstraneni html znacek """

    def __init__(self):
        """konstruktor"""
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        """krmi se daty"""
        self.fed.append(d)

    def feed(self, data):
        """nic, pro pylint"""
        return HTMLParser.feed(self, data)

    def reset(self):
        """nic, pro pylint"""
        return HTMLParser.reset(self)

    def get_data(self):
        """vraci ocisteny feed"""
        return ''.join(self.fed)

    @staticmethod
    def strip_tags(html):
        """stripper"""
        s = Stripper()
        s.feed(html)
        return s.get_data()

def load_page(url):
    """nacte stranku"""
    with urlopen(url) as response:
        return response.read().decode("utf8")
class Page:
    """ Cela stranka """

    def __init__(self, html_page):
        self.words = []
        text = Stripper.strip_tags(html_page)
        words = re.findall(r'\b[A-Z]+\b', text, re.UNICODE)
        words.sort()

        for i, word in enumerate(words):
            self.words.append(Word(word, i + 1))

    def get_rank(self):
        """vraci rank cele straky"""
        rank = 0
        for word in self.words:
            rank += word.get_rank()
        return rank

    def get_size(self):
        """vraci pocet jmen"""
        return len(self.words)


def load_config():
    """nacte konfiguraci"""
    with open('config.json', encoding="utf8") as data_file:
        return json.load(data_file)


def run_sript():
    """spusti skript"""
    url = load_config()['url']
    try:
        page = Page(load_page(url))
        rank = page.get_rank()
        size = page.get_size()
        print('Celkovy ranking:')
        print(rank)
        print('Pocet jmen:')
        print(size)
    except urllib.error.URLError:
        print('Spojeni nedostupne')


if __name__ == '__main__':
    run_sript()
