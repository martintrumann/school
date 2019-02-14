import random

money = 100
print("Let's play!")
game = True
while game == True:
	cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

	pcards = [random.choice(cards), random.choice(cards)]
	dcards = [random.choice(cards), random.choice(cards)]

	# Losing conditions
	if money < 0:
		print("You're in debt, Good luck paying it off")
		break
	elif money == 0:
		print("You ran out of money, but at least you don't have a debt")
		break
	# Bet 
	print("You have", str(money) + "\u0024")
	bet = None
	while not bet:
		bet = input("What's your bet: ")
		if not bet:
			print("insert bet")
		elif bet == "max":
			bet = money
	money -= int(bet)

	# Round start
	print("")
	round = True
	while round == True: 
		print("Dealers card is", ', '.join(dcards[1]))
		print("Your cards are", ', '.join(pcards))

		phand = 0
		dhand = 0

		# Player Choice
		i = input("Hit, Stand or Leave: ")		
		if i == "H" or i == "h" or i == "Hit" or i == "hit":
			newcard = random.choice(cards)
			pcards.append(newcard)
			print("Your new card is", newcard)
			input()
		elif i == "L" or i == "l" or i == "leave" or i == "leave":
			print("Good game! You made", str(money) + "\u0024")
			game == False
			break
		else:
			print("You decided to stand")
			round = False
			print("Dealer's cards are", ", ".join(dcards))
		
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

		print("your hands total is", phand)
		if phand > 21:
			print("You're Bust, Bet's gone")
			break
		elif phand == 21:
			print("Excacly 21, you're lucky")
		
		# Dealers hand
		if round == False:
			for c in dcards:
				if c == "A":
					continue
				elif c == "J" or c == "Q" or c == "K":
					dhand += 10
				else:
					dhand += int(c)

			for c in dcards:
				if c == "A":
					if dhand + 11 > 17 and dhand + 11 < 21:
						dhand += 11
					else:
						dhand += 1

		# winning calculation
		if round == False:
			if phand > dhand:
				print("you win! Bet's doubled")
				money += 2 * int(bet)
			else:
				print("You lost!")
				round = False
