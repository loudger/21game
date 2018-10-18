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


class Person:

    # Конструктор игрока
    def __init__(self, name = 'noname', money = 1000):
        self.hand = []
        self.add_hand_element()
        # hand = [{ 'hand_cards':[] , 'hand_to_much':False } , ... }
        self.money = money
        self.name = name

    # Добавить руку в случае сплита.
    def add_hand_element(self):
        self.hand.append({'hand_cards':[], 'hand_to_much':False})

    # Удаляет все карты из руки
    def refresh(self):
        self.hand.clear()

    # Берёт одну или больше карт из колоды
    def get_card(self, deck, num_hand = 0, count = 1):
        for i in range(count):
                self.hand[num_hand]['hand_cards'].append(deck.get_one_card())

    # Делает ставку
    def betting(self, bet):
        while True:
        # try:
            assert (bet > 0 and bet <= self.money)  #В неверном случае выдаёт исключение AssertionError
            self.money -= bet
            return bet
        # except AssertionError:
        #     pass

    # Логика игры за диллера
    def diller_logic(self, deck):
        while self.points_in_hand() <= 16:
            self.get_card(deck)
        if self.points_in_hand() > 21:
            self.hand[0]['hand_to_much'] = True

    # Проверка на сплит
    def checkup_split(self, limit_money, num_hand = 0):
        if len(self.hand[num_hand]['hand_cards']) == 2 and self.money > limit_money:
            if cost_card(self.hand[num_hand]['hand_cards'][0]) == cost_card(self.hand[num_hand]['hand_cards'][1]):
                return True
        return False

    # Проверка на удвоение
    def checkup_dubl(self, limit_money, num_hand = 0):    #Пересиписывать из-за сплита
        if len(self.hand[num_hand]['hand_cards']) == 2 and self.money > limit_money:
            return True
        return False

    # Раздвоить карты (сплит)
    def split_cards(self, deck ,num_hand = 0):
        self.add_hand_element()
        self.hand[num_hand + 1]['hand_cards'].append(self.hand[num_hand]['hand_cards'][1])
        self.hand[num_hand]['hand_cards'].pop(1)
        self.get_card(deck, num_hand = 1)
        self.get_card(deck)

    # Возвращает количество очков в руке
    def points_in_hand(self, num_hand = 0):   #Пересиписывать из-за сплита
        points = 0
        count_ace = 0
        for item in self.hand[num_hand]['hand_cards']:
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
            if points > 21:
                self.hand[num_hand]['hand_to_much'] = 1
        return points

    # Выбор действия (хватит, ещё, удвоить, сплит)
    def move(self, limit_money, num_hand = 0, move_code):
        possibility = 2     #По стандарту дано 2 действия (Хватит, Ещё)
        if self.checkup_dubl(limit_money, num_hand):
            possibility = 3
            if self.checkup_split(limit_money, num_hand) and len(self.hand) == 1 :
                possibility = 4
        return self.set_move_code(move_code, possibility)

    # Функция, которая устанавливает, что будет делать player
    def set_move_code(self, move_code, possibility):
        if move_code > 0 and move_code <= possibility:
            return move_code
        else:
            raise ValueError
