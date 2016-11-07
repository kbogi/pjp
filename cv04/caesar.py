"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""


def encrypt(word, offset):
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    
    offset %= 26
    abc='abcdefghijklmnopqrstuvwxyz'
    ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all = abc+ABC
    allOff = abc[offset:] + abc[:offset] + ABC[offset:] + ABC[:offset]
    return word.translate(word.maketrans(all, allOff))


def decrypt(word, offset):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    return encrypt(word, -offset)
