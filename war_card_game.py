from typing import List
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.shuffled_deck = []

    def create_deck(self) -> List[str]:
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        symbols = ["♣", "♠", "♦", "♥"]
        for value in values:
            for symbol in symbols:
                self.deck.append(value + symbol)
    
    # def remove_card(self) -> List[str]:
    #     self.deck.pop(0)

    def shuffle_deck(self) -> List[str]:
        # shuffled_deck = random.shuffle(self.deck)
        # return shuffled_deck
        self.shuffled_deck = self.deck[:]  # Make a copy of the original deck
        random.shuffle(self.shuffled_deck)
        return self.shuffled_deck

    
    def get_deck(self) -> List[str]:
        return self.deck

class Player:
    def __init__(self, shuffled_deck):
        self.shuffled_deck = shuffled_deck
        self.player_deck = []
        self.opponent_deck = []

    def split_into_two(self):
        # print(self.shuffled_deck)
        midpoint = len(self.shuffled_deck) // 2
        player_deck = self.shuffled_deck[:midpoint]
        opponent_deck = self.shuffled_deck[midpoint:]
        self.player_deck = player_deck
        self.opponent_deck = opponent_deck

        # return player_deck, opponent_deck

class Table:
    ...


def main():
    deck = Deck()
    deck.create_deck()

    shuffled_deck = deck.shuffle_deck()
    # print("Shuffled Deck:", shuffled_deck)

    player = Player(shuffled_deck)
    player.split_into_two()
    print(player.opponent_deck, player.player_deck)



if __name__ == "__main__":
    main()
