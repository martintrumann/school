num = input("sisesta number: ")

num1 = int(num[0]) + int(num[2]) + int(num[4]) + int(num[6]) + int(num[8]) + int(num[10])

num2 = num1 * 3

num3 = int(num[1]) + int(num[3]) + int(num[5]) + int(num[7]) + int(num[9])+ num2

M = num3 % 10

if M == 0:
    fin = 0
else:
    fin = 10 - M

print(fin)