import random

face = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
suit = ('C', 'S', 'D', 'H')
activePlayers = []
deck = []
players = ['Naman', 'CrimeMasterGOGO', 'Bulla',
           'Modiji', 'Doodhwala', 'Homer Simpson', 'Ibu hatela']
pot = 0


class card():
    def __init__(self):
        pass

    def printCard(self):
        print(self.face, self.suit)

    def makecard(self, f, s):
        self.face = f
        self.suit = s


class player():
    pile = 100000
    name = 'Player'
    card1 = card()
    card2 = card()
    card3 = card()

    def __init__(self):
        pass

    def setPlayerDetails(self, name, buyin=10000):
        self.pile = buyin
        self.name = name

    def printPlayer(self):
        print(self.name, self.pile)

    def makeBet(self, betAmount):
        self.pile -= betAmount
        pot += betAmount


def firstBet():
    pass


def makeDeck():
    for i in suit:
        for j in face:
            newcard = card()
            newcard.makecard(j, i)
            deck.append(newcard)


def dealCards():
    for i in players:
        card1 = random.choice(deck)
        deck.remove(card1)
        card2 = random.choice(deck)
        deck.remove(card2)
        card3 = random.choice(deck)
        deck.remove(card3)
        newplayer = player()
        newplayer.card1 = card1
        newplayer.card2 = card2
        newplayer.card3 = card3
        newplayer.setPlayerDetails(i)
        activePlayers.append(newplayer)


def showPlayers():
    for i in activePlayers:
        i.printPlayer()
        i.card1.printCard()
        i.card2.printCard()
        i.card3.printCard()


if __name__ == "__main__":
    makeDeck()
    dealCards()
    showPlayers()
