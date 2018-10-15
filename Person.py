from Deck import Deck


# Значимость карты
def cost_card(card):
    if isinstance(card, str):
        if card == 'T':
            cost = 11
        else:
            cost = 10
    else:
        cost = card
    return cost


class Person():

    # Конструктор игрока
    def __init__(self, name = 'noname', money = 1000):
        self.hand = []
        self.money = money
        self.to_much = False
        self.name = name

    # Удаляет все карты из руки
    def refresh(self):          #Переписывать из-за сплита
        self.hand.clear()
        self.to_much = False

    # Берёт одну или больше карт из колоды
    def get_card(self, deck, count = 1, split = False):
        for i in range(count):
            # if split:
            #     self.split_hand.append(deck.get_one_card())
            # else:
                self.hand.append(deck.get_one_card())

        # Делает ставку
    def betting(self):
        while True:
            try:
                bet = int(input('Ваша ставка: '))
                assert (bet > 0 and bet <= self.money)
                print ('Осталось:{}-{}={}'.format(self.money, bet, self.money - bet))
                self.money -= bet
                return bet
            except:
                print ('Ошибка ввода')

    # Логика игры за диллера
    def diller_logic(self, deck):
        while self.points_in_hand() <= 16:
            self.get_card(deck)
            print (self.hand,'-', self.points_in_hand())
        if self.points_in_hand() > 21:
            self.to_much = True

    # Проверка на сплит
    def checkup_split(self, limit_money):
        if len(self.hand) == 2 and self.money > limit_money:
            if cost_card(self.hand[0]) == cost_card(self.hand[1]):
                return True
        return False

    # Проверка на удвоение
    def checkup_dubl(self, limit_money):    #Пересиписывать из-за сплита
        if len(self.hand) == 2 and self.money > limit_money:
            return True
        return False

    # Раздвоить карты (сплит)
    def split_cards(self):
        self.split_hand = []
        self.split_to_much = False
        self.split_hand.append(self.hand[1])
        self.hand.pop(1)
        self.get_card(split = False)
        self.get_card(split = True)

    # Выводит количество очков в руке
    def points_in_hand(self, split_hand = False):   #Пересиписывать из-за сплита
        points = 0
        count_ace = 0
        if split_hand:
            for item in self.split_hand:
                points = self.count_points(item)
                if points > 21:
                    self.split_to_much = 1
        else:
            for item in self.hand:
                self.count_points(item)
                if points > 21:
                    self.to_much = 1
        return points

    #Считает количесво очков в руке
    def count_points(self, item):
        if isinstance(item, str):
            if item == 'T':
                points += 11
                count_ace += 1
            else:
                points += 10
        else:
            points += item
        while points > 21:
            if count_ace > 0:
                points -= 10
                count_ace -= 1
            else:
                break
        return points


    # Выбор действия (хватит, ещё, удвоить, сплит)
    def move(self, limit_money):
        possibility = 2
        print ('1. Хватит')
        print ('2. Ещё')
        if self.checkup_dubl(limit_money):
            possibility = 3
            print ('3. Удвоить')
            if self.checkup_split(limit_money):
                possibility = 4
                print ('4. Сплит(Не реализован)')
        while True:
            try:
                move_code = int(input('>>>'))
                if move_code > 0 and move_code <= possibility:
                    return move_code
                else:
                    raise Exception
            except:
                print ('Ошибка ввода')
