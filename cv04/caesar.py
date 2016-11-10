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
    abec = 'abcdefghijklmnopqrstuvwxyz'
    abec_v = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_n = abec+abec_v 
    all_off = abec[offset:] + abec[:offset] + abec_v[offset:] + abec_v [:offset]
    return word.translate(word.maketrans(all_n, all_off))


def decrypt(word, offset):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    return encrypt(word, -offset)
