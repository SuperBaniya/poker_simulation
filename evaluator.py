from poker import *

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
    if(a.suit == b.suit and b.suit == c.suit):
        color = 1
    seq = sequence(a, b, c)
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
