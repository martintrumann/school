nimi = input("mis on sinu nimi: ")

print("Tere", nimi)

elukoht= input("Kus sa elad: ")

if elukoht == "Saaremaa":
    print("Ma elan ka seal!")

vanus = int(input("kui vana sa oled?"))

if vanus < 18:
    print("Sa ei saa veel autot juhtida!")
elif vanus == 18:
    print("Palju õnne täisealiseks saamisel!")
elif vanus < 18:
    print("Sa võid autot juhtida!")