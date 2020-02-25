import random


face = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['C', 'S', 'D', 'H']


class card():
    def __init__(self):
        self.face = random.choice(face)
        self.suit = random.choice(suit)


class player(card):
    playerCards = []

    def __init__(self):
        self.playerCards[0] = card()
        self.playerCards[1] = card()
