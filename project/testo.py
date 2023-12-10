k = input('inp: ')
cm = 0
for el in ["{", "}", ":"]: cm = cm + 1 if el in k else el
if cm == len(k): print("Содержиться")


