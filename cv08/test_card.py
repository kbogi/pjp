"""testy"""

from unittest import TestCase
from card import Card


class TestCard(TestCase):
    """
    testy
    """

    def test_init(self):
        """
        konstruktor
        :return:
        """
        rank = 0
        suit = 'piky'
        try:
            Card(rank, suit)
            self.fail()
        except (TypeError, ValueError):
            pass
        except:
            self.fail()

        rank = 14
        suit = 'piky'
        try:
            Card(rank, suit)
            self.fail()
        except (TypeError, ValueError):
            pass
        except:
            self.fail()

        rank = 1
        suit = 'pilky'
        try:
            Card(rank, suit)
            self.fail()
        except (TypeError, ValueError):
            pass
        except:
            self.fail()

        rank = 1
        suit = 'piky'
        try:
            Card(rank, suit)
        except:
            self.fail()

    def test_rank(self):
        """
        test rank
        :return:
        """
        result = 5
        self.assertEqual(Card(5, 'piky').rank(), result)

    def test_suit(self):
        """
        test suit
        :return:
        """
        result = 'p'
        self.assertEqual(Card(5, 'piky').suit(), result)

    def test_black_jack_rank(self):
        """ test jack """
        self.assertTrue(Card(5, 'piky') > Card(1, 'piky'))
        self.assertFalse(Card(5, 'piky') > Card(7, 'piky'))

        self.assertTrue(Card(5, 'piky') >= Card(1, 'piky'))
        self.assertTrue(Card(10, 'piky') >= Card(13, 'piky'))
        self.assertFalse(Card(5, 'piky') >= Card(7, 'piky'))

        self.assertTrue(Card(10, 'piky') == Card(13, 'piky'))
        self.assertFalse(Card(5, 'piky') == Card(7, 'piky'))
        self.assertFalse(Card(10, 'piky') != Card(13, 'piky'))
        self.assertTrue(Card(5, 'piky') != Card(7, 'piky'))


        self.assertTrue(Card(9, 'piky') < Card(13, 'piky'))
        self.assertFalse(Card(10, 'piky') < Card(1, 'piky'))

        self.assertTrue(Card(5, 'piky') <= Card(9, 'piky'))
        self.assertTrue(Card(12, 'piky') <= Card(10, 'piky'))
        self.assertFalse(Card(10, 'piky') <= Card(7, 'piky'))

    def test_str(self):
        """test toString"""
        result = 'eso piky'
        self.assertEqual(format(Card(1, 'piky')), result)