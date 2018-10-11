from Deck import Deck
from Person import Person


class Bank():

    # Конструктор
    def __init__(self):
        self.bank = {}

    # Назначает диллера
    def indicate_diller(self, diller):
        self.diller = diller

    # Ставка сделана и сохранена в словаре
    def bet_in_bank(self, human):
        self.bank[human] = human.betting()

    # Удваивает ставку
    def double_bet(self,human):
        for key in self.bank:
            if key == human:
                human.money-= self.bank[key]
                self.bank[key] *= 2

    # Возвращает деньги при выигрыше
    def rewarding(self, human):
        for key in self.bank:
            if key == human:
                human.money += 2 * self.bank[key]
                self.diller.money -= self.bank[key]

    # Возвращает деньги, если была ничья
    def return_money(self, human):
        for key in self.bank:
            if key == human:
                human.money += self.bank[key]

    # Отдаёт деньги диллеру, при проигрыше игрока
    def diller_is_winer(self, player):
        for key in self.bank:
            if key == player:
                self.diller.money += self.bank[key]

    # Возвращает значение (сколько было поставлено)
    def return_value(self, player):
        for key in self.bank:
            if key == player:
                return self.bank[key]

    # Обновляется каждый раунд
    def refresh_bank(self):
        self.bank.clear()
