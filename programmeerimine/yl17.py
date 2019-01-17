from random import *
while True:
    num = randint(1,3)
    #(0 = käärid,) 1 = kivi, 2 = paber, 3 = käärid, (4 = kivi)
    user = input("(k)ivi, (p)aber, (k)äärid või (l)ahku: ")
    
    if user == "kivi" or user == "k":
        usernum = 1
    elif user == "paber" or user == "p":
        usernum = 2
    elif user == "kaarid" or user == "käärid" or user == "k":
        usernum = 3
    elif user == "lahku" or user == "l":
        break
    print(num, usernum)
    if usernum == num:
        print("viik")
    elif num + 1 == usernum or usernum + 2 == num:
        print("sinu võit!")
    elif num - 1 == usernum or usernum - 2 == num:
        print("minu võit!")
    print()
        