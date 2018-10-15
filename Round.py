from Person import Person
from Bank import Bank
from Deck import Deck
import random
import copy

class Round():

    # Конструктор класса раунд
    def __init__(self, all_players, diller, bank, deck):
        self.bank = bank
        # self.bank.refresh_bank()
        self.count_player = len(all_players)
        self.all_players = copy.copy(all_players)
        self.players = copy.copy(all_players)
        self.players.remove(diller)
        self.diller = diller
        self.deck = deck

    # Ход игрока
    def players_move(self):
        for player in self.players:
            self.show_diller_cards()
            while True:
                print('\n', player.name)
                print(player.hand, '-', player.points_in_hand())
                move_code = player.move(self.bank.return_value(player))
                if move_code == 1:
                    break
                elif move_code == 2:
                    player.get_card(self.deck)
                    player.points_in_hand()
                    if player.to_much == True:
                        print('\n', player.name)
                        print(player.hand, '-', player.points_in_hand())
                        self.player_lose(player)
                        break
                elif move_code == 3:
                    player.get_card(self.deck)
                    self.bank.double_bet(player)
                    print('\n', player.name)
                    print(player.hand, '-', player.points_in_hand())
                    player.points_in_hand()
                    if player.to_much == True:
                        print('\n', player.name)
                        print(player.hand, '-', player.points_in_hand())
                        self.player_lose(player)
                    break
                else:
                    player.split_cards()
                    self.bank.bet_in_split_bank(player)
                    self.start_split_move(player)

    # Реализация сплита
    def start_split_move(self, player):
        print ('Первая рука {} - {}\nВторая рука {} - {}'.format(player.hand, player.points_in_hand(),player.split_hand, player.points_in_hand(split = True)))
        while True:
            print('\n', player.name)
            print(player.hand, '-', player.points_in_hand())
            move_code = player.move(self.bank.return_value(player))
            if move_code == 1:
                break
            elif move_code == 2:
                player.get_card(self.deck)
                player.points_in_hand()
                if player.to_much == True:
                    print('\n', player.name)
                    print(player.hand, '-', player.points_in_hand())
                    self.player_lose(player)
                    break
            elif move_code == 3:
                player.get_card(self.deck)
                self.bank.double_bet(player)
                print('\n', player.name)
                print(player.hand, '-', player.points_in_hand())
                player.points_in_hand()
                if player.to_much == True:
                    print('\n', player.name)
                    print(player.hand, '-', player.points_in_hand())
                    self.player_lose(player)
                break
        while True:
            print('\n', player.name)
            print(player.split_hand, '-', player.points_in_hand(split = True))
            move_code = player.move(self.bank.return_value(player))
            if move_code == 1:
                break
            elif move_code == 2:
                player.get_card(self.deck, split = True)
                player.points_in_hand(split = True)
                if player.split_to_much == True:
                    print('\n', player.name)
                    print(player.split_hand, '-', player.points_in_hand(split = True))
                    # self.player_lose(player) переделать
                    break
            elif move_code == 3:
                player.get_card(self.deck, split = True)
                # self.bank.double_bet(player) Переделать
                print('\n', player.name)
                print(player.split_hand, '-', player.points_in_hand(split = True))
                player.points_in_hand(split = True)
                if player.split_to_much == True:
                    print('\n', player.name)
                    print(player.split_hand, '-', player.points_in_hand(split = True))
                    # self.player_lose(player) Переделать
                break

    # Показать карты диллера
    def show_diller_cards(self, hide = True):
        print('\nКарты диллера')
        if hide == True:
            print ([self.diller.hand[0], '?'])
        else:
            print (self.diller.hand,'-',self.diller.points_in_hand())

    # Игроки делают ставки
    def push_bets(self):
        for player in self.players:
            print()
            print ('{}, Ваш банк: {}'.format(player.name, player.money))
            self.bank.bet_in_bank(player)

    # Раздать карты игрокам
    def give_cards_to_players(self):
        for player in self.all_players:
            player.get_card(self.deck, 2)


    # Сравнивает очки
    def comprasion_points(self):
        if self.diller.to_much:
            for player in self.players:
                if player.to_much == False:
                    self.result_win(player)
        else:
            for player in self.players:
                if player.to_much == False:
                    if player.points_in_hand() > self.diller.points_in_hand():
                        self.result_win(player)
                    elif player.points_in_hand() < self.diller.points_in_hand():
                        self.player_lose(player)
                    else:
                        self.result_draw(player)

    # Указать диллера для банка
    def indicate_diller_for_bank(self):
        self.bank.indicate_diller(self.diller)

    # Реализация выигрыша
    def result_win(self, player):
        print()
        print('{},{}={} > Вы выиграли!'.format(player.name, player.hand, player.points_in_hand()))
        self.bank.rewarding(player)

    # Если игрок проиграл
    def player_lose(self, player):
        print()
        print('{},{}={} > Вы проиграли!'.format(player.name, player.hand, player.points_in_hand()))
        # self.players.remove(player)
        self.bank.diller_is_winer(player)

    # Реализация ничьи
    def result_draw(self,player):
        print()
        print('{},{}={} > Ничья!'.format(player.name, player.hand, player.points_in_hand()))
        self.bank.return_money(player)

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
            if player.to_much == False:
                count += 1
        return count



    # Раунд
    # def play_round(self):
    #     self.give_cards_to_players()
    #     self.players_move()


















        #
