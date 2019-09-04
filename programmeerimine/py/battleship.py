from random import randint
game = True
round = True
while game == True:
	board = []
	for i in range(10):
		board.append("~~~~~~~~~~")

	def printboard():
		for row in board:
			print(row)

	'''
	class Ship():
		x = None
		y = None
		def __init__(self, x, y):
			self.x = x
			self.y = y

	def make_ship(x, y):
		ship = Ship(x, y)
		return ship

	s1 = make_ship(randint(0, 11), randint(0, 11))
	'''

	shots = []
	while round == True:
		shot = input("where to shoot (x, y): ")
		shots.append(shot)
		game = False
		round = False
