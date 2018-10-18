from Person import Person
from Bank import Bank
from Deck import Deck
import random
import copy

class Round():

    # Конструктор класса раунд
    def __init__(self, all_players, diller, bank, deck):
        self.bank = bank
        self.count_player = len(all_players)
        self.all_players = copy.copy(all_players)   #Все игроки
        self.players = copy.copy(all_players)       #Все игроки раунда кроме дилера
        self.players.remove(diller)
        self.diller = diller
        self.deck = deck

    # Ход игрока
    def players_move(self, set_players = None, split = False):
        if set_players is None:     # Если не установлено по каким игрокам проходить в раунде
            players = self.players
        else:
            players = [set_players]
        for player in players:
            for num_hand in range(len(player.hand)):    #Проходит по всем рукам всех игроков
                self.show_diller_cards()
                while True:
                    if player.points_in_hand(num_hand) == 21:
                        break
                    move_code = player.move(self.bank.return_value(player, num_hand), num_hand = num_hand)
                    if move_code == 1:
                        break
                    elif move_code == 2:
                        player.get_card(self.deck, num_hand = num_hand)
                        player.points_in_hand(num_hand)
                        if player.hand[num_hand]['hand_to_much'] == True:
                            self.player_lose(player, num_hand)
                            break
                    elif move_code == 3:
                        player.get_card(self.deck, num_hand = num_hand)
                        self.bank.double_bet(player, num_hand)
                        player.points_in_hand(num_hand)
                        if player.hand[num_hand]['hand_to_much'] == True:
                            self.player_lose(player, num_hand)
                        break
                    else:
                        player.split_cards(self.deck)
                        self.bank.bet_in_split_bank(player)
                        self.players_move(player, split = True)
                        break

    # Показать карты диллера
    def show_diller_cards(self, hide = True):
        if hide == True:
            return [self.diller.hand[0]['hand_cards'][0], '?']
        else:
            return self.diller.hand[0]['hand_cards']

    # Игроки делают ставки
    def push_bets(self):
        for player in self.players:
            self.bank.bet_in_bank(player)

    # Раздать карты игрокам
    def give_cards_to_players(self):
        for player in self.all_players:
            player.get_card(self.deck, count = 2)


    # Сравнивает очки
    def comprasion_points(self):
        if self.diller.hand[0]['hand_to_much']:
            for player in self.players:
                for num_hand in range(len(player.hand)):
                    if player.hand[num_hand]['hand_to_much'] == False:
                        self.result_win(player, num_hand)
        else:
            for player in self.players:
                for num_hand in range(len(player.hand)):
                    if player.hand[num_hand]['hand_to_much'] == False:
                        if player.points_in_hand(num_hand) > self.diller.points_in_hand():
                            self.result_win(player, num_hand)
                        elif player.points_in_hand(num_hand) < self.diller.points_in_hand():
                            self.player_lose(player, num_hand)
                        else:
                            self.result_draw(player, num_hand)

    # Указать диллера для банка
    def indicate_diller_for_bank(self):
        self.bank.indicate_diller(self.diller)

    # Реализация выигрыша
    def result_win(self, player, num_hand):
        self.bank.rewarding(player, num_hand)
        return ('{},{}={} > Вы выиграли!'.format(player.name, player.hand[num_hand]['hand_cards'], player.points_in_hand(num_hand)))

    # Если игрок проиграл
    def player_lose(self, player, num_hand):
        self.bank.diller_is_winer(player, num_hand)
        return ('{},{}={} > Вы проиграли!'.format(player.name, player.hand[num_hand]['hand_cards'], player.points_in_hand(num_hand)))

    # Реализация ничьи
    def result_draw(self,player, num_hand):
        self.bank.return_money(player, num_hand)
        return ('{},{}={} > Ничья!'.format(player.name, player.hand[num_hand]['hand_cards'], player.points_in_hand(num_hand)))

    # Ход диллера
    def diller_turn(self):
        self.show_diller_cards(hide = False)
        if self.count_to_much() > 0:
            self.diller.diller_logic(self.deck)

    # Обновление карт, to_much
    def refresh_round(self):
        self.players = copy.copy(self.all_players)
        for player in self.all_players:
            player.refresh()
            player.add_hand_element()
        self.players.remove(self.diller)
        self.deck.refresh_cards()
        self.bank.refresh_bank()

    # Красиво выводит имя игроков, кто ещё не проиграл
    # Использовалось для дебагов
    def list_name_players(self):
        for i in self.players:
            yield i.name

    # используется для подсчёта игроков, которые не выбыли из игры
    # Это делается на случай, если все переберут и чтобы диллер не продолжал играть
    def count_to_much(self):
        count = 0
        for player in self.players:
            for num_hand in range(len(player.hand)):
                if player.hand[num_hand]['hand_to_much'] == False:
                    count += 1
        return count



    # Раунд
    # def play_round(self):
    #     self.give_cards_to_players()
    #     self.players_move()


















        #
