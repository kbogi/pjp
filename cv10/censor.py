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
    return re.sub(mezery, ' ', re.sub(html_tag, ' ', text))


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
                    repl += '#'
                return repl
        return to_check.group()
    return re.sub(r'[\w-]+', replace_word, text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help=Strings.HELP_TEXTS['i'])
    parser.add_argument("-l", "--list", help=Strings.HELP_TEXTS['l'])
    parser.add_argument("-c", "--clean", action='store_true', help=Strings.HELP_TEXTS['c'])
    parser.add_argument("-o", "--output", help=Strings.HELP_TEXTS['o'])
    args = parser.parse_args()
    words = []
    if args.list is not None:
        words = load_list(args.list)
    if args.output is not None:
        out = FileOutput(args.output)
    else:
        out = ConsoleOutput()
    if args.input is not None:
        with open(args.input, 'r', encoding='utf-8') as soubor:
            text = soubor.read()
            if args.clean:
                text = strip_html(text)
            text = replace_words(text, words)
            out.write(text)
