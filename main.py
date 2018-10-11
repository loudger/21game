import random
import copy


def Yes_No():
	while True:
		try:
			check = input ('[y/n] > ')
			if check == 'y' or check == 'n':
				return check
			else:
				raise Exception
		except:
			print ('Ошибка ввода')


class Bank():
	def __init__(self):
		self.bets = {}

	def bet_in_bank(self, human):
		self.bets[human] = human.betting()

	def rewarding(self, human, roundResult):
		for key in self.bets:
			if key == human:
				if roundResult == 'w':
					human.money += 2 * self.bets[key]
					bankir.money -= self.bets[key]
				elif roundResult == 'l':
					bankir.money += self.bets[key]
				else:
					human.money += self.bets[key]


def take_one_card (list):
	x = random.choice(list)
	list.remove(x)
	return x

def gameover(st, human):
	bank.rewarding(human, st)
	if st == 'w':
		print ('	YOU WIN!')
		history['win'] += 1
		print(history)
	elif st == 'l':
		print ('	YOU LOSE!')
		history['lose'] += 1
		print(history)
	elif st == 'd':
		print ('	DROW!!!')
		print(history)
	else:
		pass
	print (human.money)
	human.refresh()
	bankir.refresh()


class person():
	hand = []
	toMuch = 0
	def __init__(self, money = 1000):
		self.money = money
		print (self.money)

	def get_hand(self,lst):
		self.hand = copy.copy(lst)

	def refresh(self):
		self.hand.clear()
		self.toMuch = 0

	def __cmp__(): 
		pass

	def points(self):
		x = 0
		flag = 0
		for item in self.hand:
			if isinstance(item, str):
				if item == 'T':
					x += 11
					flag += 1
				else:
					x += 10
			else:
				x += item
			while x > 21:
				if flag > 0:
					x -= 10
					flag -= 1
				else:
					break
		if x > 21:
			self.toMuch = 1
		return x

	def betting(self):
		while True:
			try:
				bet = int(input ('Ваша ставка: '))
				assert(bet>0)
				self.money -= bet
				return bet
			except:
				print ('Ошибка ввода')


	def logic(self, deck, another):
		if self.toMuch == 0:
			myPoint = self.points()
			if myPoint == 21:
				return 'ok'
			elif myPoint <= another.points():
				while self.points() <= another.points():
					if self.points() == another.points() and self.points() > 14:
						break
					else:
						self.hand.append(take_one_card(deck))
			print ('loading...')
			print (bankir.hand)
			print (bankir.points())
			return 'ok'
		else:
			pass

	def turn(self, deck):
		x = 'y'
		while x == 'y' and self.points() < 22:
			print ('Take one more card?')
			x = Yes_No()
			if x == 'y':
				self.hand.append(take_one_card(deck))
				print (self.hand)
				print (self.points())
				if self.points() > 21:
					self.toMuch = 1



history = {'win' : 0, 'lose' : 0}

basic_deck = [2 , 2 , 2 , 2, 3 ,3 ,3 ,3 ,4 ,4 ,4 ,4 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,7 ,7 ,7 ,7 ,8 ,8 ,8 ,8 ,9 ,9 ,9 ,9 
,10 ,10 ,10 , 10, 'V', 'V', 'V', 'V','D' ,'D' ,'D' ,'D' ,'K','K','K','K', 'T', 'T', 'T', 'T',]
print ('Игра 21, Нажмите Enter, чтобы начать')
input ()
print ('Игра начинается')
check = True


bankir = person(money = 5000)
Iam = person()

while check:
	cards = copy.copy(basic_deck)
	bank = Bank()
	bank.bet_in_bank(Iam)
	Iam.get_hand([take_one_card(cards),take_one_card(cards)])
	print (Iam.money)
	bankir.get_hand([take_one_card(cards),take_one_card(cards)])
	print('-Bankir:')
	print (bankir.hand)
	print (bankir.points())
	print ('\n-You:')
	print (Iam.hand)
	print(Iam.points())
	Iam.turn(cards)
	if Iam.toMuch == 1:
		print('111111111111')
		gameover('l',Iam)
	else:
		print ('\n-Bankir:')
		bankir.logic(cards, Iam)
		print ('-You:')
		print (Iam.hand)
		print(Iam.points())
		if bankir.toMuch == 1 and Iam.toMuch == 0:
			gameover('w',Iam)
		elif bankir.toMuch == 0 and Iam.toMuch == 1:
			print('22222222')
			gameover('l',Iam)
		elif bankir.toMuch == 1 and Iam.toMuch == 1:
			gameover('d',Iam)
		else:
			if bankir.points() > Iam.points():
				gameover('l',Iam)
			elif bankir.points() < Iam.points():
				print('3333333')
				gameover('w',Iam)
			else:
				gameover('d',Iam)

	print('\nDo you wanna play more?')
	check = Yes_No()
	if check == 'y':
		check = True
		print ('---//---//---//---//---//---//---//---//---//---')
	else:
		check = False
		print ('Thanks for playing!')