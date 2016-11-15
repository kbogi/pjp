# -*- coding: utf-8 -*-

"""
Modul pro ukol 5 
nevim co to má za problém, pylint hlásí neco nekonvencniho na 1. řádku
"""
import re

def split_text(text):
    """
    deleni vety na pole slov
    """
    return re.findall(r'[\w-]+', text, re.UNICODE)
