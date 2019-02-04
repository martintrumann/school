import math
a = float(input("sisesta reaalosa: "))
b = float(input("sisesta imaginaarosa ilma i-ta: "))

r = a * a + b * b
if math.sqrt(r) % 1 == 0:
	r = round(math.sqrt(r))
	print("moodul on", r)
else:
	r = "\u221a" + str(round(r))
	print("moodul on", r)

if b == 0 and a > 0:
	fiideg = 0
elif a == 0 and b > 0:
	fiideg = 90
elif b == 0 and a < 0:
	fiideg = 180
elif a == 0 and b < 0:
	fiideg = 270
else:
	fiirad = math.atan(b / a)
	fiideg = math.degrees(fiirad)
	while fiideg > 360:
		fiideg = fiideg - 360
	if a > 0 and b > 0: # I sector
		while fiideg > 90 or fiideg < 0:
			fiideg = fiideg + 180
	elif a < 0 and b > 0: # II sector
		while fiideg > 180 or fiideg < 90:
			fiideg = fiideg + 180
	elif a < 0 and b < 0: # III sector
		while fiideg > 270 or fiideg < 180:
			fiideg = fiideg + 180 
	elif a > 0 and b < 0: # IV sector
		while fiideg > 360 or fiideg < 270:
			fiideg = fiideg + 180
	else:
		print("how did you get here? it should be impossible")

fiideg = round(fiideg)
print("fii on", fiideg)

# trigonomeetriline kuju

print(str(r) +  "(cos" + str(fiideg) + "\u00b0 + i * sin" + str(fiideg) + "\u00b0)")
