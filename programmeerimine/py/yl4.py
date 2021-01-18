num1 = input("arv1: ")
num2 = input("arv2: ")
num3 = input("arv3: ")

maxx = num1

if num2 > maxx:
    maxx = num2
elif num3 > maxx:
    maxx = num3

print(maxx)
