import random

game = True
money = 100
print("Let's play!")
while game == True:
	cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

	pcards = [random.choice(cards), random.choice(cards)]
	dcards = [random.choice(cards), random.choice(cards)]

	phand = 0
	dhand = 0

	# Bet 
	print("You have", str(money) + "\u0024")
	bet = None
	while not bet:
		bet = input("What's your bet: ")
		if not bet:
			print("insert bet")
	money -= int(bet)

	# Round start
	print("")
	round = True
	while round == True: 
		print("Dealers card is", ', '.join(dcards[1]))
		print("Your cards are", ', '.join(pcards))
		# Player Choice
		i = input("Hit, Stand or Leave: ")		
		if i == "H" or i == "h" or i == "Hit" or i == "hit":
			newcard = random.choice(cards)
			pcards.append(newcard)
			print("Your new card is", newcard)
			input()
		elif i == "L" or i == "l" or i == "leave" or i == "leave":
			print("Good game! You made", str(money) + "\u0024")
			game = False
			round = False
		else:
			print("You decided to stand")
			round = False
			print("Dealer's cards are", ", ".join(dcards))
			print("your total was", phand)
		
		# players total
		for c in pcards:
			if c == "A":
				Aval = int(input("A is 1 or 11: "))
				if Aval == 1:
					phand += 1
				elif Aval == 11:
					phand += 11
			elif c == "J" or c == "Q" or c == "K":
				phand += 10
			else:
				phand += int(c)
		print(phand)
		if phand > 21:
			print("You're Bust, Bet's gone")
			round = False
		elif phand == 21:
			print("Excacly 21, you're lucky")
		
		# Dealers hand
		
		for c in dcards:
			if c == "A":
				continue
			elif c == "J" or c == "Q" or c == "K":
				phand += 10
			else:
				phand += int(c)

		for c in dcards:
			if c == "A":
				if dhand + 11 > 17 and dhand + 11 < 17:
					dhand += 11
				else:
					dhand += 1

		# Losing conditions
		if money < 0:
			print("You're in debt, Good luck paying it off")
			game = False
			round = False
		elif money == 0:
			print("You ran out of money, but at least you don't have a debt")
			game = False
			round = False
