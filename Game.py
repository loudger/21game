from Round import Round
from Bank import Bank
from Person import Person
from Deck import Deck
import random


class Game():

    # Конструктор для игры
    def __init__(self, bank):
        self.bank = bank
        self.players_list = []
        self.start_game()
        self.diller is None

    # Создаёт игроков и даёт им имена
    def create_players(self):
        print('Имена должны не повторяться и состоять минимум из трёх симловом')
        if self.count_player >= 2:
            first_player = Person(name = self.input_name('первого'))
            self.players_list.append(first_player)
            second_player = Person(name = self.input_name('второго'))
            self.players_list.append(second_player)
            if self.count_player >= 3:
                third_player = Person(name = self.input_name('третьего'))
                self.players_list.append(third_player)
                if self.count_player >= 4:
                    fourth_player = Person(name = self.input_name('четвертого'))
                    self.players_list.append(fourth_player)
                    if self.count_player == 5:
                        fifth_player = Person(name = self.input_name('пятого'))
                        self.players_list.append(fifth_player)

    # Проверка на правильно введёное имя
    # Имена не повторяются
    def input_name(self, number_of_player):
        while True:
            try:
                name = str(input('Имя {} игрока:'.format(number_of_player)))
                if len(name) >= 3 and len(name) <= 14:
                    for another_name in self.players_list:
                        if another_name.name == name:
                            raise Exception
                    return name
                else:
                    raise Exception
            except Exception:
                print('Ошибка ввода')

    # Случайно определяет диллера
    def random_diller(self):
        self.diller = random.choice(self.players_list)
        print('Выбран диллер! Сегодня это - {}\n'.format(self.diller.name))
        return self.diller

    # Назначает следующего диллера
    def next_diller(self):
        ind = self.players_list.index(self.diller)
        if ind != len(self.players_list)-1:
            self.diller = self.players_list[ind+1]
        else:
            self.diller = self.players_list[0]
        self.show_diller()

    # Выводит имя диллера
    def show_diller(self):
        print('\nВ этом раунде дилер {}!!'.format(self.diller.name))

    # Убирает человека из игры
    def delete_player(self, player):
        self.players_list.remove(player)

    # Убирает человека из игры, если он остался без денег
    def players_no_money(self):
        for player in self.players_list:
            if player.money <= 0 and player != self.diller:
                self.players_list.remove(player)
                print('\nИгрок {} выбывает из игры'.format(player.name))

    # Убирает дилера, если он остался без денег
    def diller_no_money(self):
        if self.diller.money <= 0:
            self.players_list.remove(self.diller)

    # Проверка: остался ли хоть кто-то играть,кроме одного человека
    def left_one_player(self):
        if len(self.players_list) == 1:
            print('Остался только {}, игра закончена'.format(self.players_list[0].name))
            self.end_game()

    def all_checks(self):
        self.players_no_money()
        self.next_diller()
        self.diller_no_money()
        self.left_one_player()


    # Начало игры
    def start_game(self):
        input('Нажмите Enter, чтобы играть в BlackJack')
        while True:
            try:
                self.count_player = int(input('Введите количество игроков(2 - 5):'))
                if self.count_player >= 2 and self.count_player <= 5:
                    break
                else:
                    raise Exception
            except:
                print ('Повторите попытку')
        self.create_players()
        self.random_diller()

    # Конец игры
    def end_game(self):
        raise SystemExit

    # Зацикливание раундов
    def cycle_rounds(self):
        while True:
            round = Round(self.players_list, self.diller, self.bank, Deck())
            round.indicate_diller_for_bank()
            round.push_bets()
            round.give_cards_to_players()
            round.players_move()
            round.diller_turn()
            round.comprasion_points()
            round.refresh_round()
            self.all_checks()
