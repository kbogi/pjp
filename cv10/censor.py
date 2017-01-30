# -*- coding: utf-8 -*-
import re
from FileOutput import FileOutput
from ConsoleOutput import ConsoleOutput
import Strings
import argparse

"""
@TODO - vyřešit úkol 10. - filtrování textu
-i, --input : soubor který má být upraven (běžný text)
-l, --list : soubor se seznamem zakázaných slov - jedno slovo jeden řádek
-c, --clean : přepínač vyčištění souboru od html - viz. dále
-o, --output: výstupní soubor, pokud není volba použita, tak vypsat data na obrazovku
-h, --help : nápověda - o čem program je a jak se ovládá
"""


def strip_html(text):
    html_tag = re.compile('<[^>]*>')
    mezery = re.compile('\s+')
    new_line = re.compile(r'\n')

    def check_newline(match):
        if new_line.search(match.group()):
            return '\n'
        return ' '
    text = re.sub(html_tag, ' ', text)
    text = re.sub(r'(^\s+)|(\s+$)', '', text)
    return re.sub(mezery, check_newline, text)


def load_list(soubor):
    words = []
    data = open(soubor, 'r', encoding='utf-8')
    for line in data:
        words.append(line.replace('\n', ''))
    data.close()
    return words


def replace_words(text, words):
    def replace_word(to_check):
        for word in words:
            if to_check.group() == word:
                repl = ''
                for ch in word:
                    if ch:
                        pass
                    repl += '#'
                return repl
        return to_check.group()

    return re.sub(r'[\w-]+', replace_word, text)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-i", "--input", help=Strings.HELP_TEXTS['i'])
    PARSER.add_argument("-l", "--list", help=Strings.HELP_TEXTS['l'])
    PARSER.add_argument("-c", "--clean", action='store_true', help=Strings.HELP_TEXTS['c'])
    PARSER.add_argument("-o", "--output", help=Strings.HELP_TEXTS['o'])
    ARGS = PARSER.parse_args()
    WORDS = []
    if ARGS.list is not None:
        WORDS = load_list(ARGS.list)
    if ARGS.output is not None:
        OUT = FileOutput(ARGS.output)
    else:
        OUT = ConsoleOutput()
    if ARGS.input is not None:
        with open(ARGS.input, 'r', encoding='utf-8') as f:
            TEXT = f.read()
            if ARGS.clean:
                TEXT = strip_html(TEXT)
            TEXT = replace_words(TEXT, WORDS)
            OUT.write(TEXT)
