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
        return self.value + self.suit
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
    def __init__(self, computer=False):
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
            # self.card = hiddencard.pop()
            print(self.card[1])
            print("hidden")
        # else:
        #     for Cards in self.card:
        #         print(Cards)

class Rungame:
    def __init__(self):
        pass
    def play(self):
        # playing = True
        # while playing:
            self.deck = Deck()
            self.deck.shuffle()
            self.player_hand = Hand()
            self.computer_hand = Hand(computer=True)
            for i in range(2):
                self.player_hand.add(self.deck.deal())
                self.computer_hand.add(self.deck.deal())

            print("Your hand: ")
            self.player_hand.display()
            print("Computer hand: ")
            self.computer_hand.display()
            choice = input("Hit/Stick: ")
            if choice == "Hit":
                self.player_hand.add(self.deck.deal())
                self.player_hand.display()
                if self.playerOver():
                    print("Computer wins")
            else:
                player_hand_value = self.player_hand.get_value()
                computer_hand_value = self.computer_hand.get_value()

    def playerOver(self):
        return self.player_hand.get_value > 21



if __name__ == "__main__":
    game = Rungame()
    game.play()
            