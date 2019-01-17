dict = {
    "eesnimi": "Martin",
    "perekonnanimi": "Trumann",
    "sünniaasta": 2002,
    "elukoht": "Saadu Talu",
    "lemmik magustoit": "Prantsuse sokolaadikook",
}

print(dict["eesnimi"])
print(dict.get("perekonnanimi"))
dict["lemmik magustoit"] = "jäätis"

print()

for i in dict:
    print(i,"-", dict[i])
print()
print(dict)
    
if "isikukood" in dict:
    print("isikukood on olemas")

print ()

print(len(dict))

print()

print(len(dict["eesnimi"]))

dict.pop("sünniaasta")
