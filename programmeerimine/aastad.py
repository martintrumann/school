aasta = int(input("sisesta aastaarv: "))

if aasta % 4 == 0 or aasta % 400 == 0 and aasta % 400 != 0:
    print("Liigaasta!")
else:
    print("ei ole liigasta!")