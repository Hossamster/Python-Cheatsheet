from random import shuffle
class Card(object):
    def __init__(self,value,suit):
        self.suit = suit.capitalize()
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck():
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value,suit)  for suit in suits for value in values]
        print(self.cards)

    def __repr__(self):
        return self.count()

    def count(self):
       return len(self.cards)

    # # FIXME:
    def _deal(self,num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise TypeError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self,hand_size):
        return self._deal(hand_size)
    
    # def shuffle(self):
    #     if len(Deck.lst):
    #         raise ValueError("Only full decks can be shuffled")
    
     
# c = Card(9,'Hearts')
# print(c)

d = Deck()
# print(d.count())
# print(d.__repr__())
# print(d._deal(23))
d.shuffle()
print(d.deal_hand(3))


