from typing import List
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.player_deck = []
        self.bot_deck = []

        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        # values = ["2", "3", "4", "5", "6"]
        symbols = ["♣", "♠", "♦", "♥"]
        for value in values:
            for symbol in symbols:
                self.deck.append(value + symbol)

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck

    def split_into_two(self):
        midpoint = len(self.deck) // 2
        self.player_deck = self.deck[:midpoint]
        self.bot_deck = self.deck[midpoint:]
    
    

class Player:
    def __init__(self, deck):
        self.hand = deck

    def deal_card(self):
        return self.hand.pop()

    def add_card(self, card):
        self.hand.append(card)
    
    def add_cards(self, cards):
        for card in cards:
            self.hand.append(card)


class Card:
    def __init__(self, card):
        self.rank = card[:-1]

    ranks_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __lt__(self, other):
        return self.ranks_order.index(self.rank) < self.ranks_order.index(other.rank)

    def __gt__(self, other):
        return self.ranks_order.index(self.rank) > self.ranks_order.index(other.rank)

    def __eq__(self, other):
        return self.ranks_order.index(self.rank) == self.ranks_order.index(other.rank)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.shuffled_deck = self.deck.shuffle_deck()
        self.deck.split_into_two()
        self.human = Player(self.deck.player_deck)
        self.bot = Player(self.deck.bot_deck)
        self.round_count = 0

    def play_round(self):
        self.round_count += 1
        round_outcome = ""
        
        while True:
            start_round = input("Press 'Enter' to play")
            if start_round == "":
                break

        h_dealt_card = self.human.deal_card()
        b_dealt_card = self.bot.deal_card()

        h_card = Card(h_dealt_card)
        b_card = Card(b_dealt_card)

        table_ui = Table_UI(b_dealt_card, h_dealt_card, self.round_count)
        
        if h_card > b_card:
            round_outcome = "win"
            self.human.add_card(h_dealt_card)
            self.human.add_card(b_dealt_card)
            table_ui.print_round(round_outcome)
        elif h_card < b_card:
            round_outcome = "lose"
            self.bot.add_card(h_dealt_card)
            self.bot.add_card(b_dealt_card)
            table_ui.print_round(round_outcome)
        else:
            round_outcome = "tie"
            self.human.add_card(h_dealt_card)
            self.bot.add_card(b_dealt_card)
            table_ui.print_round(round_outcome)
            self.play_war_round()

        print(f"Player's cards: {len(self.human.hand)}")
        print("vs")
        print(f"Bot's cards: {len(self.bot.hand)}")

    def play_war_round(self):
        print("War!")
        if not self.check_cards_for_war():
            return 

        war_cards = []
        for _ in range(3):
            h_war_dealt_card = self.human.deal_card()
            war_cards.append(h_war_dealt_card)

            b_war_dealt_card = self.bot.deal_card()
            war_cards.append(b_war_dealt_card)


        h_war_dealt_card = self.human.deal_card()
        b_war_dealt_card = self.bot.deal_card()

        war_cards.append(h_war_dealt_card)
        war_cards.append(b_war_dealt_card)


        h_war_card = Card(h_war_dealt_card)
        b_war_card = Card(b_war_dealt_card)

        table_ui = Table_UI(h_war_dealt_card, b_war_dealt_card, self.round_count)
        # print(f"WAR CARDS: {war_cards}")
        if h_war_card > b_war_card:
            round_outcome = "War win"
            self.human.add_cards(war_cards)
            table_ui.print_war_round(round_outcome)
        elif h_war_card < b_war_card:
            round_outcome = "War lose"
            self.bot.add_cards(war_cards)
            table_ui.print_war_round(round_outcome)
        else:
            round_outcome = "War tie"
            table_ui.print_war_round(round_outcome)
            self.play_war_round()

    def check_cards_for_war(self):
        if len(self.human.hand) < 4:
            print("Bot wins! Player does not have enough cards to continue the war.")
            return False 
        elif len(self.bot.hand) < 4:
            print("Player wins! Bot does not have enough cards to continue the war.")
            return False
        return True

    def start_game(self):
        while True:
            self.play_round()
            if len(self.human.hand) == 0:
                print("Bot wins! Player has run out of cards.")
                return
            elif len(self.bot.hand) == 0:
                print("Player wins! Bot has run out of cards.")
                return

class Table_UI:
    def __init__(self, bot_card, human_card, round_count):
        self.bot_card = bot_card
        self.human_card = human_card
        self.round_count = round_count

    def print_round(self, round_outcome):
        print("-----------------------------")
        print(f"Current round: {self.round_count}")
        print(f"You - {self.human_card} vs {self.bot_card} - Opponent")
        print(f"Round result: {round_outcome}")
        print("-----------------------------")

    def print_war_round(self, round_outcome):
        print("-----------------------------")
        print(f"Current round: {self.round_count} (War)")
        print(f"You - {self.human_card} vs {self.bot_card} - Opponent")
        print(f"War result: {round_outcome}")



def main():
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
