k1 = int(input("esimese külje pikkus: "))
k2 = int(input("teise külje pikkus: "))
k3 = int(input("kolmas külje pikkus: "))

sides=[k1, k2, k3]
sides.sort()

if sides[-1] > sides[0] + sides[1]:
    print("vöimatu")

elif k1 == k2 == k3:
    print("võrdkülgne")

elif k1 == k2 != k3 or k1 != k2 == k3 or k1 != k3 == k2 or k1 == k3 != k2:
    print("võrdhaarne")

elif k1 != k2 or k2 != k3 or k3 != k1:
    print("erikülgne")