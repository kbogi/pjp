# -*- coding: utf-8 -*-

"""
úkol 9. - zpracování HTML
"""

from html.parser import HTMLParser
import re
import urllib.request

class MyParser(HTMLParser):
    """ dictionary """
    dic = {}
    mail = set()
    em = re.compile('[a-z1-9\\.]+@[a-z1-9\\.]+')


    def __init__(self, page):
        """constructor"""
        self.page = page
        MyParser.dic[self.page] = []
        HTMLParser.__init__(self)

    def feed(self, data):
        """hledani adres"""
        HTMLParser.feed(self, data)
        for email in re.findall(MyParser.em, data):
            MyParser.mail.add(email)


    def handle_starttag(self, tag, attrs):
        """handle tags"""
        # Only parse the 'anchor' tag.
        em = MyParser.em

        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, print it.
                if name == "href":
                    p = re.compile('https?://')
                    m = re.compile(r'mailto:(.*)')
                    mm = m.match(value)
                    if p.match(value):
                        pass
                    elif mm:
                        address = re.sub('[^a-z1-9@\\.]', '', mm.group(1))
                        if em.match(address):
                            MyParser.mail.add(address)
                    else:
                        if value not in MyParser.dic:
                            MyParser.dic[self.page].append(value)
                            baseadr = 'https://jirivrany.github.io' \
                                      '/pjp_html_data/'
                            with urllib.request.urlopen(
                                            baseadr + value) as res:
                                html = res.read().decode("utf8")
                                nparser = MyParser(value)
                                nparser.feed(html)


if (__name__ == '__main__'):
    with urllib.request.urlopen('https://jirivrany.git'
                                'hub.io/pjp_html_data/') as response:
        HTML = response.read().decode("utf8")
        PARSER = MyParser('index.html')
        PARSER.feed(HTML)
        F = open('scrap_result.txt', 'w')
        F.write(str(MyParser.dic) + '\n\n')
        for mail in MyParser.mail:
            F.write(mail + '\n')
        F.close()
