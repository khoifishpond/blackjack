import random
from card import Card

class Deck:


    def __init__(self):
        self.deck = []
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += card.__str__() + '\n'
        return deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
