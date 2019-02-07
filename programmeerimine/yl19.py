import random

game = True
money = 100
print("Let's play!")
while game == True:
	cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

	pcards = [random.choice(cards), random.choice(cards)]
	dcards = [random.choice(cards), random.choice(cards)]
	# round start
	round = True
	while round == True: 
		print("You have", str(money) + "\u0024")

		print(pcards, sep=" ", end=" ", flush=True)
		# Player Choice
		i = input("Hit, Stand or Leave: ")		
		if i == "H" or i == "h" or i == "Hit" or i == "hit":
			pcards.append(random.choice(cards))
		elif i == "L" or i == "l" or i == "leave" or i == "leave":
			print("Good game! You made", str(money) + "\u0024")
			game = False
			round = False
		else:
			print("You decided to stand")


		# Losing conditions
		if money < 0:
			print("You're in debt, Good luck paying it off")
			game = False
		elif money == 0:
			print("You ran out of money, but at least you don't have a debt")
			game = False
