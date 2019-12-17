import random

Cardvalue = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J" ,"Q", "K"]
Suittype = ["Hearts", "Diamonds", "Spades", "Clubs"]

class Cards:
    def __init__(self, value, suit):
        assert value in Cardvalue
        self.value = value
        assert suit in Suittype
        self.suit = suit
    def __repr__(self):
        return self.value + "of" + self.suit
    def ace(self):
        return self.value == "A"
    def acevalue(self):
        if self.ace():
            value = 11
        else:
            try:
                value = int(self.value)
            except ValueError:
                value = 10
        return value

class Deck:
    def __init__(self):
        self.card = [Cards(value, suit) for value in Cardvalue for suit in Suittype]
    def shuffle(self):
        if len(self.card) > 1:
            return random.shuffle(self.card)
    def deal(self):
        if len(self.card) > 1:
            return self.card.pop(0)
 
class Hand:
    def __init__(self, computer):
         self.computer = computer
         self.card = []
         self.value = 0
    def add(self, card):
        self.card.append(card)
    def calculate(self):
        self.value = 0
        ace = "A"
        acevalue = False
        for card in self.card:
            if card.value.isnumeric():
                self.value += int(card.value)
            elif self.value > 21 and ace > 1:
                acevalue -= 1
                self.value -= 10
            else:
                if self.value == "A":
                    acevalue = True
                    self.value += 11
                else:
                    self.value += 10
    def get_value(self):
        self.calculate
        return self.value
    def display(self):
        # hiddencard = deck(hidden = True)
        if Cards in self.card:
            print(Cards)
        elif self.computer:
            print("hidden")
            # self.card = hiddencard.pop()
            print(self.card[1])
        # else:
        #     for Cards in self.card:
        #         print(Cards)


