#Import shuffle from random module
from random import shuffle

#Declares a Card class
class Card:

    #Initializes suit and value variables
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #Prints following string instead of the address of the object
    def __repr__(self):
        return f"{self.value} of {self.suit}"

#Declare a Deck class
class Deck:

    #Crates a deck of cards, each a Card object
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    #Returns the number of cards left in the deck
    def count(self):
        return len(self.cards)

    #Prints following string instead of the address of the object
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    #Deals a number of cards for the deck
    def _deal(self, num):
        
        #List to store dealt cards
        lst = []

        #Raises error if deck is empty
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        #Deals the rest of the deck if the deck doesn't have as many cards as the user wants to deal
        if num > self.count():
            for i in range(self.count()):
                lst.append(self.cards.pop())
        #Deals cards if deck has the amount of cards specified
        else:
            for i in range(num):
                lst.append(self.cards.pop())
        #Returns the dealt cards
        return lst
    
    #Used _deal to deal a single card
    def deal_card(self):
        return(self._deal(1)[0])

    #Randomly shuffles the deck
    def shuffle(self):
        #Raises error if deck is not full
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled.")
        else:
            shuffle(self.cards)
            return self.cards
        
    #Deals a specific number of cards
    def deal_hand(self, num):
        return self._deal(num)
