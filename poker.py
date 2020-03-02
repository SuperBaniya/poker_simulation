import random
import evaluator

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


strength = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    "A": 14
}


def colourSequence(a, b, c):
    color = 0
    if(a.suit == b.suit and b.suit == c.suit):
        color = 1
    seq = sequence(a.face, b.face, c.face)
    if(seq and color):
        return 1
    else:
        return 0


def sequence(a, b, c):
    l = [strength[a], strength[b], strength[c]]
    l.sort()
    sequence = 0
    if(l[0]+1 == l[1]and l[1]+1 == l[2]):
        sequence = 1
    return sequence


def evaluateCards(card1, card2, card3):
    score = 0
    cards = [card1, card2, card3]
    highcard = 2
    for i in cards:
        if strength[i.face] > highcard:
            highcard = strength[i.face]

    if card1.face == card2.face and card2.face == card3.face:
        score = 6

    elif colourSequence(card1, card2, card3):
        score = 5

    elif sequence(card1.face, card2.face, card3.face):
        score = 4

    elif card1.suit == card2.suit and card2.suit == card3.suit:
        score = 3

    elif card1.face == card2.face:
        score = 2
        highcard = strength[card1.face]

    elif card1.face == card3.face:
        score = 2
        highcard = strength[card1.face]

    elif card2.face == card3.face:
        score = 2
        highcard = strength[card2.face]

    return score, highcard


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
        print(evaluateCards(i.card1, i.card2, i.card3))


if __name__ == "__main__":
    makeDeck()
    dealCards()
    showPlayers()
