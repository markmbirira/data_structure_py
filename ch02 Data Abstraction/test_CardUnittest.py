#!/usr/bin/env python

import unittest
from Card import Card


class TestCard(unittest.TestCase):
    """Unit tests for Card ADT."""

    def test_constructor(self):
        pass

    def test_suit_char(self):
        ace_of_clubs = Card(1, 'c')
        king_of_diamonds = Card(13, 'd')
        jack_of_spades = Card(11, 's')
        two_of_hearts = Card(2, 'h')

        self.assertEqual(ace_of_clubs.suit(), 'c')
        self.assertEqual(king_of_diamonds.suit(), 'd')
        self.assertEqual(jack_of_spades.suit(), 's')
        self.assertEqual(two_of_hearts.suit(), 'h')

    def test_rank_number(self):
        ace_of_clubs = Card(1, 'c')
        king_of_diamonds = Card(13, 'd')
        jack_of_spades = Card(11, 's')
        two_of_hearts = Card(2, 'h')

        self.assertEqual(ace_of_clubs.rank(), 1)
        self.assertEqual(king_of_diamonds.rank(), 13)
        self.assertEqual(jack_of_spades.rank(), 11)
        self.assertEqual(two_of_hearts.rank(), 2)

    def test_rank_name(self):
        ace_of_clubs = Card(1, 'c')
        king_of_diamonds = Card(13, 'd')
        jack_of_spades = Card(11, 's')
        two_of_hearts = Card(2, 'h')

        self.assertEqual(ace_of_clubs.rankName(), 'Ace')
        self.assertEqual(king_of_diamonds.rankName(), 'King')
        self.assertEqual(jack_of_spades.rankName(), 'Jack')
        self.assertEqual(two_of_hearts.rankName(), 'Two')

    def test_suit_name(self):
        ace_of_clubs = Card(1, 'c')
        king_of_diamonds = Card(13, 'd')
        jack_of_spades = Card(11, 's')
        two_of_hearts = Card(2, 'h')

        self.assertEqual(ace_of_clubs.suitName(), 'Clubs')
        self.assertEqual(king_of_diamonds.suitName(), 'Diamonds')
        self.assertEqual(jack_of_spades.suitName(), 'Spades')
        self.assertEqual(two_of_hearts.suitName(), 'Hearts')

    def test_str(self):
        ace_of_clubs = Card(1, 'c')
        king_of_diamonds = Card(13, 'd')
        jack_of_spades = Card(11, 's')
        two_of_hearts = Card(2, 'h')

        self.assertEqual(str(ace_of_clubs), 'Ace of Clubs')
        self.assertEqual(str(king_of_diamonds), 'King of Diamonds')
        self.assertEqual(str(jack_of_spades), 'Jack of Spades')
        self.assertEqual(str(two_of_hearts), 'Two of Hearts')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
