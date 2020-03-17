from poker import *


def evaluateCards(card1, card2, card3):
    score = 0
    cards = [card1, card2, card3]
    highcard = 2
    pairhighcard = 2
    hand = "highcard"
    for i in cards:
        if strength[i.face] > highcard:
            highcard = strength[i.face]
            pairhighcard = highcard

    if card1.face == card2.face and card2.face == card3.face:
        score = 6
        hand = 'Trio'

    elif colourSequence(card1, card2, card3):
        score = 5
        hand = 'Pure Sequence'

    elif sequence(card1.face, card2.face, card3.face):
        score = 4
        hand = 'Sequence'

    elif card1.suit == card2.suit and card2.suit == card3.suit:
        score = 3
        hand = 'Colour'

    elif card1.face == card2.face:
        score = 2
        pairhighcard = strength[card1.face]
        hand = 'pair'

    elif card1.face == card3.face:
        score = 2
        pairhighcard = strength[card1.face]
        hand = 'pair'
    elif card2.face == card3.face:
        score = 2
        pairhighcard = strength[card2.face]
        hand = 'pair'
    return score, highcard, hand, pairhighcard

    def makeMove(card1, card2, card3):
        score = evaluateCards(card1, card2, card3)[0]
        if(score < 3 and score > 0):
            return "MinBet"
        elif(score >= 3):
            return "Raise"