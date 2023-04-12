#!/usr/bin/env python3.10

import random

class BlackJack():

	###	TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO ##
		### TODO: dealer shows one card :TODO
		### TODO: create functions for dealer play, bust and blackjack :TODO
		### TODO: make it so that player cards all REMAIN with their indexes :TODO
		### TODO: declare all variables globally as empty types, for reference on their intended types :TODO
		### TODO: consider a NEW naming scheme :TODO
	###	TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO ##

	scs = [] # spade cards
	hcs = [] # heart cards
	ccs = [] # club cards
	dcs = [] # diamond cards
	sfv = [] # spade face value
	hfv = [] # heart face value
	cfv = [] # club face value
	dfv = [] # diamond face value
	cs = [] # cards
	fvs = [] # face values
	fv = str() # face value
	c = str() # card
	pc1 = [] # player card 1
	pc2 = [] # player card 2
	pc3 = [] # player card 3
	pc4 = [] # player card 4
	pc5 = [] # player card 5
	dc1 = [] # dealer card 1
	dc2 = [] # dealer card 2
	dc3 = [] # dealer card 3
	dc4 = [] # dealer card 4
	dc5 = [] # dealer card 5

	def give_card(self):
		spade = {"SA": "🂡", "S2": "🂢", "S3": "🂣", "S4": "🂤", "S5": "🂥", "S6": "🂦", "S7": "🂧", "S8": "🂨", "S9": "🂩", "S10": "🂪" ,"SJ": "🂫", "SQ": "🂭", "SK": "🂮"}
		heart = {"HA": "🂱", "H2": "🂲", "H3": "🂳", "H4": "🂴", "H5": "🂵", "H6": "🂶", "H7": "🂷", "H8": "🂸", "H9": "🂹", "H10": "🂺", "HJ": "🂻", "HQ": "🂽", "HK": "🂾"}
		club = {"CA": "🃑", "C2": "🃒", "C3": "🃓", "C4": "🃔", "C5": "🃕", "C6": "🃖", "C7": "🃗", "C8": "🃘", "C9": "🃙", "C10": "🃚" ,"CJ": "🃛", "CQ": "🃝", "CK": "🃞"}
		diamond = {"DA": "🃁", "D2": "🃂", "D3": "🃃", "D4": "🃄", "D5": "🃅", "D6": "🃆", "D7": "🃇", "D8": "🃈", "D9": "🃉", "D10": "🃊" ,"DJ": "🃋", "DQ": "🃍", "DK": "🃎"}
		# We can correlate the index numbers of these resulting lists with the index numbers of the next bit:
		s_cards = list(spade.values())
		h_cards = list(heart.values())
		c_cards = list(club.values())
		d_cards = list(diamond.values())
		# The index numbers of these resulting lists can correlate with the index numbers of the above 4 lists:
		s_face_value = list(spade.keys())
		h_face_value = list(heart.keys())
		c_face_value = list(club.keys())
		d_face_value = list(diamond.keys())
		# To get an entire deck of cards and facevalues, with their indexes preserved, we append the lists:
		cards = list(s_cards + h_cards + c_cards + d_cards)
		face_values = list(s_face_value + h_face_value + c_cards + d_cards)
		# A test to make sure we get the correct face_values from cards:
		r = random.randint(1,52) - 1
		card = cards[r]
		face_value = face_values[r]
		return card, face_value

	def hand_value(self, hand, hit):
		self.hand = hand
		face_cards = ["10"."J","Q","K"]
		ace = "A"
		if ininstance(hand, list):
			for c in hand:
				if ininstance(c, str):
					c = c[1:]
					if c in face_cards:
						c = 10
					elif c == ace:
						c = 11
					else:
						c = int(c)
					hand.append(c)
			hand = sum(hand)
			return hand_value

	def start_deal(self):
		start = input("Deal a game of BlackJack?  (y/n)?")
		if start != "y":
			print("Cya!")
			exit()
		else:
			# each a list with two strings, card and face_value
			player_card_1 = self.give_card()
			dealer_card_1 = self.give_card()
			player_card_2 = self.give_card()
			dealer_card_2 = self.give_card()

			dealer_hand = self.hand_value(list(dealer_card_1[1], dealer_card_2[1]), 0)
			player_hand = self.hand_value(list(player_card_1[1], player_card_2[1]), 0)

			dealer_cards = str(dealer_card_1[0] + " " + dealer_card_2[0])
			player_cards = str(player_card_1[0] + " " + player_card_2[0])

			if int(player_hand) > 21:
				# bust()
				pass
			elif int(player_hand) == 21:
				# dealer()
				pass
			else:

		###	### TODO: dealer shows one card :TODO ###
		### TODO: dealer shows one card :TODO ### ###
		###	### TODO: dealer shows one card :TODO ###
		### TODO: dealer shows one card :TODO ### ###
		###	### TODO: dealer shows one card :TODO ###

				# execute delivery of cards
				print(f"Your cards are: {player_cards} [value: {player_hand}]\r\n")
				self.hit_or_stay(self, dealer_cards, player_cards, dealer_hand, player_hand)

	def hit_or_stay(self, dealer_cards, player_cards, dealer_hand, player_hand):
		hit_or_stay = input("Hit or Stay?\r\n")
		hits = ["Hit", "hit", "h", "H", "Hit me", "hit me", "Hit me!", "Hit Me!", "Hit Me", "tap", "++", "y", "Y"]
		stays = ["Stay", "stay", "s", "hold", "Hold", "h", "H", "n", "N", "--"]
		
		if hit_or_stay in hits:
			player_card_3 = self.give_card()
			c = player_card_3[1:]
			face_cards = ["10"."J","Q","K"]
			ace = "A"
			
			if c in face_cards:
				c = 10
			elif c == ace:
				c = 11
			else:
				c = player_card_3[1:]

			self.player_cards = player_cards
			player_cards = str(player_cards + " " + player_card_3[0])
			player_hand = int(player_hand + c)
			
			if player_hand == 21:
				# dealer()
				pass
			elif player_hand > 21:
				# bust()
				pass
			else:
				hit_or_stay(self, dealer_cards, player_cards, dealer_hand, player_hand)

		if hit_or_stay in stays:
			# dealer()
			pass

	def bust(self):
		pass

	def dealer():
		pass

	def blackjack(self, player_cards):
		pass


	# ♠ = cards.spade
	# ♥ = cards.heart
	# ♣ = cards.club
	# ♦ = cards.diamond