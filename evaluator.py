from poker import *


def evaluateCards(card1, card2, card3):
    if card1.face == card2.face or card2.face == card3.face or card1.face == card3.face:
        ans = 'pair'
