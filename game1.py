import random

class Cards:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return self.value, self.suit

class Deck:
    def __init__(self):
        self.card = [Cards(value, suit) for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J" ,"Q", "K"] for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]]
    def shuffle(self):
        if len(self.card) > 1:
            return random.shuffle(self.card)
    def deal(self):
        if len(self.card) > 1:
            return self.card.pop(0)
 