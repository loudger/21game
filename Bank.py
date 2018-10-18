from Deck import Deck
from Person import Person


class Bank:

    # Конструктор
    def __init__(self):
        self.bank = {}
        # bank = {[bet],[bet,bet],[bet],...}

    # Назначает диллера
    def indicate_diller(self, diller):
        self.diller = diller

    # Ставка сделана и сохранена в словаре
    def bet_in_bank(self, player, num_hand = 0):
        if num_hand == 0:
            self.bank[player] = [player.betting()]
        else:
            self.bank[player].insert(num_hand, self.bank[player][0])

    # Сплитует ставку
    def bet_in_split_bank(self, player, num_hand = 0):
        try:
            if player in self.bank:
                player.money -= self.bank[player][num_hand]
                self.bank[player].append(self.bank[player][num_hand])
            else:
                raise Exception('Ошибка, игрок {} не делал ставку'.format(player.name))
        except Exception as e:
            pass

    # Удваивает ставку
    def double_bet(self, player, num_hand):
        try:
            if player in self.bank:
                player.money -= self.bank[player][num_hand]
                self.bank[player][num_hand] *= 2
            else:
                raise Exception('Ошибка, игрок {} не делал ставку'.format(player.name))
        except Exception as e:
            pass


    # Возвращает деньги при выигрыше
    def rewarding(self, player, num_hand):
        try:
            if player in self.bank:
                player.money += 2 * self.bank[player][num_hand]
                self.diller.money -= self.bank[player][num_hand]
            else:
                raise Exception('Ошибка, игрок {} не делал ставку'.format(player.name))
        except Exception as e:
            pass

    # Возвращает деньги, если была ничья
    def return_money(self, player, num_hand):
        try:
            if player in self.bank:
                player.money += self.bank[player][num_hand]
            else:
                raise Exception('Ошибка, игрок {} не делал ставку'.format(player.name))
        except Exception as e:
            pass

    # Отдаёт деньги диллеру, при проигрыше игрока
    def diller_is_winer(self, player, num_hand):
        try:
            if player in self.bank:
                self.diller.money += self.bank[player][num_hand]
            else:
                raise Exception('Ошибка, игрок {} не делал ставку'.format(player.name))
        except Exception as e:
            pass

    # Возвращает значение (сколько было поставлено)
    def return_value(self, player, num_hand):
        try:
            if player in self.bank:
                return self.bank[player][num_hand]
            else:
                raise Exception('Ошибка, игрок {} не делал ставку'.format(player.name))
        except Exception as e:
            pass

    # Обновляется каждый раунд
    def refresh_bank(self):
        self.bank.clear()
