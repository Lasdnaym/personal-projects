import random
import tkinter as tk

class Blackjack:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
        self.player_hand = []
        self.dealer_hand = []
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack()
        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack()
        self.player_label = tk.Label(self.root, text="Your hand: ")
        self.player_label.pack()
        self.dealer_label = tk.Label(self.root, text="Dealer's hand: ")
        self.dealer_label.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def start_game(self):
        self.player_hand = random.sample(self.cards, 2)
        self.dealer_hand = random.sample(self.cards, 2)
        self.player_label.config(text="Your hand: " + str(self.player_hand))
        self.dealer_label.config(text="Dealer's hand: [{}, X]".format(self.dealer_hand[0]))
        self.root.mainloop()

    def hit(self):
        self.player_hand.append(random.choice(self.cards))
        self.player_label.config(text="Your hand: " + str(self.player_hand))
        if self.check_bust(self.player_hand):
            self.end_game("bust")
            self.hit_button.config(state="disabled")
            self.stand_button.config(state="disabled")

    def stand(self):
        self.hit_button.config(state="disabled")
        self.stand_button.config(state="disabled")
        self.dealer_play()
        self.end_game()

    def check_bust(self, hand):
        if sum(hand) > 21:
            return True
        else:
            return False

    def dealer_play(self):
        while sum(self.dealer_hand) < 17:
            self.dealer_hand.append(random.choice(self.cards))
            self.dealer_label.config(text="Dealer's final hand: " + str(self.dealer_hand))

    def end_game(self, outcome=None):
        if outcome == "bust":
            self.result_label.config(text="You bust! Better luck next time.")
        else:
            if sum(self.player_hand) > sum(self.dealer_hand) or self.check_bust(self.dealer_hand):
                self.result_label.config(text="You win!")
            elif sum(self.player_hand) < sum(self.dealer_hand):
                self.result_label.config(text="You lose.")
            else:
                self.result_label.config(text="It's a tie.")

game = Blackjack()
game.start_game()