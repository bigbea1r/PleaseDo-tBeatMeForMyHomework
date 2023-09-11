str = str(input("Э слышъ пышы здэсь: ")).lower()
true_or_false = []
for i in range(0, round(len(str)/2)):
    if str[i] == str[(len(str)-i) - 1]:
        true_or_false.append(True)
    else:
        true_or_false.append(False)
if all(true_or_false):
    print("Ля рэално палароид.")
else:
    print("Слышышь ты бядолага! Ты чо подсунул?!")
