# Deck.py
from random import randrange
from Card import Card


class Deck(object):
    """A Deck of cards."""

    def __init__(self):
        """post: Create a 52-card deck in standard order"""
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank, suit))
        self.cards = cards

    def shuffle(self):
        """Shuffle the deck
        post: randomizes the order of cards in self"""

        n = self.size()
        cards = self.cards
        for i, card in enumerate(cards):
            pos = randrange(i, n)
            cards[i] = cards[pos]
            cards[pos] = card

    def deal(self):
        """Deal a single card
        pre: self.size() > 0
        post: Returns the next card in self, and removes it from self"""
        return self.cards.pop()

    def size(self):
        """Cards left
        post: Returns the number of cards in self"""
        return len(self.cards)
