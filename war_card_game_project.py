from typing import List
import random

class Cards:
    def __init__(self):
        self.deck = []

    def create_deck(self) -> List[str]:
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        symbols = ["♣", "♠", "♦", "♥"]
        for value in values:
            for symbol in symbols:
                self.deck.append(value + symbol)
    
    def remove_card(self) -> List[str]:
        self.deck.pop(0)

    def shuffle_cards(self) -> List[str]:
        random.shuffle(self.deck)
    
    def get_deck(self) -> List[str]:
        return self.deck




def main():
    cards = Cards()
    cards.create_deck()
    cards.remove_card()
    cards.shuffle_cards()

    print(cards.get_deck())

    
    

        



if __name__ == "__main__":
    main()
