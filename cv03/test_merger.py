# -*- coding: utf-8 -*-

import merger
"""
Py.test testy pro merger module

Pokud máte nainstalovaný program PyTest stačí ho spustit v adresáři s testem
příkazem py.test 

PyTest si sám najde testy a postará se o jejich provedení.

PyTest si můžete nainstalovat přes pip a je také součástí distribuce Anaconda
"""

def merge_tuples(line_a, line_b, line_c):
    """
    funkce merge tuples - spojujici sekvence
    """
    loc = locals()
    sl = {}
    
    index = len(loc)-1
    for key, val in loc.items():
        for node in val:
            add(sl, node[0], node[1], index)
        index -= 1
    return sl

    
def add(sl, id, val, index):
    if not( id in sl):
        sl[id] = [0,0,0]
        
    sl[id][index] = val;

