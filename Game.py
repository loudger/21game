from Round import Round
from Bank import Bank
from Person import Person
import random


class Game():

    # Конструктор для игры
    def __init__(self):
        self.start_game()
        self.players_list = []
        while True:
            try:
                self.count_player = int(input('Введите количество игроков:'))
                if self.count_player >= 2 and self.count_player <= 5:
                    break
                else:
                    raise Exception
            except:
                print ('Повторите попытку')

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
        pass

    # Начало игры
    def start_game(self):
        input('Нажмите Enter, чтобы играть в BlackJack')

    # Конец игры
    def end_game(self):
        pass

    # Зацикливание раундов
    def cycle_rounds(self):
        pass
