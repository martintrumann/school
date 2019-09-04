import random

num = random.randint(0, 1000)

print(num)

if num >= 0 and num < 10:
	print("ühekohaline")
elif num < 100:
	print("kahekohaline")
elif num < 1000:
	print("kolmekohaline")
else:
	print("What? How?")
