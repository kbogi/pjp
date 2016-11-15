# -*- coding: utf-8 -*-

"""
@author: Jiri Vrany

Pro použití je potřeba balíček py.test.
Instaluje se přes pip příkazem pip install pytest.

Zbytek je snadný, nakopírujte tento soubor do adresáře s
řešením a z příkazové řádky
spusťe test - příkazem py.test

Pytest prohledá aktuální adresář (a adresáře vnořené) a spustí
nalezené testy. Více si o tomto programu povíme na přednášce.

"""
import cestina


def test_cesky():
    """
    jenoduchy test kodovani cestiny
    """
    text = 'šíleně žluťoučký kůň'
    result = ['šíleně', 'žluťoučký', 'kůň']
    assert text.split() == result


def test_split_text():
    """
    test pro kratky text
    """
    text = """Programovací jazyk Python přispívá k
     rychlému vývoji. Python se sice snaží být intuitivní,
    ale obsahuje věci, které nejsou všední, a příliš se o nich neví.

    A nyní něco úplně jiného: jedna. Kde leží Frýdek-Místek?
    Jedna + jedna se rovná? Totéž co čtyři / dvěma!
    """

    result = [
        'Programovací',
        'jazyk',
        'Python',
        'přispívá',
        'k',
        'rychlému',
        'vývoji',
        'Python',
        'se',
        'sice',
        'snaží',
        'být',
        'intuitivní',
        'ale',
        'obsahuje',
        'věci',
        'které',
        'nejsou',
        'všední',
        'a',
        'příliš',
        'se',
        'o',
        'nich',
        'neví',
        'A',
        'nyní',
        'něco',
        'úplně',
        'jiného',
        'jedna',
        'Kde',
        'leží',
        'Frýdek-Místek',
        'Jedna',
        'jedna',
        'se',
        'rovná',
        'Totéž',
        'co',
        'čtyři',
        'dvěma']

    assert result == cestina.split_text(text)
