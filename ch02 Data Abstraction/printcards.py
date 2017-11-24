# printcards.py
# Simple test of the Card ADT

from Card import Card


def printAll():
    for suit in 'cdhs':
        for rank in range(1, 14):
            card = Card(rank, suit)
            print('Rank %s' % (card.rank()))
            print('Suit %s' % (card.suit()))
            print(card)


if __name__ == '__main__':
    printAll()
