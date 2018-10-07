import random
import copy

def takeplz (list):
	x = random.choice(list)
	list.remove(x)
	return x

def gameover(st):
	if st == 'w':
		print ('	CONGRATULATION, YOU WIN!')
		history['win'] += 1
		print(history)
	elif st == 'l':
		print ('	SORY, YOU LOSE!')
		history['lose'] += 1
		print(history)
	elif st == 'd':
		print ('	DROW!!!')
		print(history)
	else:
		pass

class person():
	hand = []
	toMuch = 0
	def __init__(self, lst):
		self.hand = lst

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

	# def logic(self, deck):
	# 	if self.toMuch == 0:
	# 		myPoint = self.points()
	# 		if myPoint == 21:
	# 			return 'Your turn'
	# 		elif myPoint < 16:
	# 			while self.points() < 16:
	# 				self.hand.append(takeplz(deck))
	# 		print ('loading...')
	# 		print (bankir.hand)
	# 		print (bankir.points())
	# 		return 'ok'
	# 	else:
	# 		pass

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
						self.hand.append(takeplz(deck))
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
			x = (input('[y/n] > '))
			if x == 'y':
				self.hand.append(takeplz(deck))
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
while check:
	cards = copy.copy(basic_deck)

	bankir = person([takeplz(cards),takeplz(cards)])
	# bankir = person(['T', 'T'])
	print('-Bankir:')
	print (bankir.hand)
	print (bankir.points())
	print ('\n-You:')
	Iam = person([takeplz(cards),takeplz(cards)])
	print (Iam.hand)
	print(Iam.points())
	Iam.turn(cards)
	if Iam.toMuch == 1:
		gameover('l')
	else:
		print ('\n-Bankir:')
		bankir.logic(cards, Iam)
		print ('-You:')
		print (Iam.hand)
		print(Iam.points())
		if bankir.toMuch == 1 and Iam.toMuch == 0:
			gameover('w')
		elif bankir.toMuch == 0 and Iam.toMuch == 1:
			gameover('l')
		elif bankir.toMuch == 1 and Iam.toMuch == 1:
			gameover('d')
		else:
			if bankir.points() > Iam.points():
				gameover('l')
			elif bankir.points() < Iam.points():
				gameover('w')
			else:
				gameover('d')
	print('\nDo you wanna play more?')
	check = input ('[y/n] > ')
	if check == 'y':
		check = True
		print ('---//---//---//---//---//---//---//---//---//---')
	else:
		check = False
		print ('Thanks for playing!')