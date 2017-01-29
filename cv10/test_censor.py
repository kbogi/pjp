# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro modul censor.py
"""
import censor, os
def test_strip_html():
    arg = '<html> <h1>vypadam uplne jako html stranka</h1><br><p>fakt ze jo</p></html>'
    result = ' vypadam uplne jako html stranka fakt ze jo '
    huu = censor.strip_html(arg)
    assert result == huu

def test_load():
    filename = 'test_fail.txt'
    f = open(filename, 'w', encoding='utf-8')
    f.write('radek\ndruhy\ntreti')
    f.close()
    result = ['radek', 'druhy', 'treti']
    list = censor.load_list(filename)
    try:
        os.remove(filename)
    except OSError:
        pass
    assert result == list

def test_replace_words():
    words = ['mistrovství', 'světa']
    text = 'Česká cyklokrosařka Kateřina Nash získala na mistrovství světa v Lucembursku bronz v závodě žen. Svůj ' \
           'první titul mezi ženami vybojovala Belgičanka Sanne Cantová, která předčila v dramatickém finiši ' \
           'favorizovanou Nizozemku Marianne Vosovou, sedminásobnou mistryni světa '
    result = 'Česká cyklokrosařka Kateřina Nash získala na ########### ##### v Lucembursku bronz v závodě žen. Svůj ' \
             'první titul mezi ženami vybojovala Belgičanka Sanne Cantová, která předčila v dramatickém finiši ' \
             'favorizovanou Nizozemku Marianne Vosovou, sedminásobnou mistryni ##### '
    assert result == censor.replace_words(text, words)