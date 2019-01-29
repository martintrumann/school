import math
a = int(input("sisesta reaalosa: "))
b = int(input("sisesta imaginaarosa ilma i-ta: "))

r = a * a  + b * b
if math.sqrt(r) % 1 == 0:
	print("moodul on", math.sqrt(r))
else:
	print("moodul on \u221a" + str(r))

if b == 0 and a > 0:
	fiideg = 0
elif a == 0 and b > 0:
	fiideg = 90
elif b == 10 and a < 0:
	fiideg = 180
elif a == 0 and b < 0:
	fiideg = 270
else:
	fiirad = math.atan(b / a)
	fiideg = math.degrees(fiirad)
	if fiideg > 360:
		fiideg = fiideg - 360
	elif a > 0 and b > 0: # I sector
		while fiideg > 90 and fiideg < 0:
			fiideg = fiideg + 180
	elif a < 0 and b > 0: # II sector
		while fiideg > 180 and fiideg < 90:
			fii = fiideg + 180
	elif a < 0 and b < 0: # III sector
		while fiideg > 270 and fiideg < 180:
			fiideg = fiideg + 180 
	elif a > 0 and b < 0: # IV sector
		while fiideg > 360 and fiideg < 270:
			fiideg = fiideg + 180
	else:
		print("how did you get here? it should be impossible")

fiideg = round(fiideg)
print("fii on", fiideg)
