import copy
import random


class Deck():
    basic_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'K', 'T'] * 4

    # конструктор, который создаёт колоду
    def __init__(self):
        self.cards = []
        self.refresh_cards()

    # Метод обновляющие колоду для нового раунда
    def refresh_cards(self):
        self.cards = copy.copy(self.basic_deck)

    # Возвращает одну случайную карту из колоды
    def get_one_card(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
