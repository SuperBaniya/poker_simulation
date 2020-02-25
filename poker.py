import random


face = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['C', 'S', 'D', 'H']


class card():
    def __init__(self):
        self.face = random.choice(face)
        self.suit = random.choice(suit)

    def printCard(self, card):
        print(self.face, self.suit)


class player(card):
    playerCards = [card(), card()]

    def __init__(self):
        pass

    def printPlayerCards(self):
        print(self.playerCards[0].face, self.playerCards[0].suit)
        print(self.playerCards[1].face, self.playerCards[1].suit)


obj = player()
obj.printPlayerCards()
