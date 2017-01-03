""" Na PJP """
class Card(object):
    """
    Karty na hraní
    """
    suits = ('srdce', 'kára', 'piky', 'trefy')
    black_jack_ranks = {1: (1, 'eso'),
                        2: (2, 'dvojka'),
                        3: (3, 'trojka'),
                        4: (4, 'ctverka'),
                        5: (5, 'petka'),
                        6: (6, 'sestka'),
                        7: (7, 'sedm'),
                        8: (8, 'osum'),
                        9: (9, 'devet'),
                        10: (10, 'deset'),
                        11: (10, 'junek'),
                        12: (10, 'dama'),
                        13: (10, 'king')}
    max = 13
    min = 1

    def __init__(self, rank, suit):
        """ konstruktor """
        self.suits.index(suit)
        if (rank < self.min or rank > self.max):
            raise TypeError('spatna hodnota')
        self.r = rank
        self.s = suit

    def rank(self):
        """ vraci rank """
        return self.r

    def suit(self):
        """ vraci suit """
        return self.s

    def black_jack_rank(self):
        """ vraci BJ rank"""
        return self.black_jack_ranks[self.r][0]

    def __lt__(self, other):
        return self.black_jack_rank() < other.black_jack_rank()
    def __le__(self, other):
        return self.black_jack_rank() <= other.black_jack_rank()
    def __eq__(self, other):
        return self.black_jack_rank() == other.black_jack_rank()
    def __ne__(self, other):
        return self.black_jack_rank() != other.black_jack_rank()
    def __gt__(self, other):
        return self.black_jack_rank() > other.black_jack_rank()
    def __ge__(self, other):
        return self.black_jack_rank() >= other.black_jack_rank()

