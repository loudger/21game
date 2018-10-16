from Deck import Deck
from Person import Person
from Round import Round
from Deck import Deck
from Game import Game
from Bank import Bank

Arthur = Person('Артур')
Maxim = Person('Максим')
deck = Deck()
bank = Bank()


game = Game()
game.create_players()

round = Round(game.players_list, game.random_diller(), bank, deck)


while True:
	round.indicate_diller_for_bank()
	round.push_bets()
	round.give_cards_to_players()
	round.players_move()
	round.diller_turn()
	round.comprasion_points()
	round.refresh_round()

