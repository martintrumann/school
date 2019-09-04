txt = input("sisiesta text: ")

list = ["a","e","i","o","u","õ","ä","ö","ü"]
n = 0

for l in list:
    for let in txt:
        if l == let:
            n = n + 1
print(n)