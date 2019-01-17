from random import *

num = randint(0, 101)
answer = False

while answer == False:
    guess = int(input("paku arv"))
    if guess == num:
        print("õige arv: ")
        answer = True
    elif num < guess:
        print("vastus on väiksem")
    elif num > guess:
        print("vastus on suurem")
        