string = input("Введите строку: ")

opening = string.count('(')

closing = string.count(')')

if opening > closing:
    print(f"Не хватает {opening - closing} закрывающей скобки!")
elif closing > opening:
    print(f"Не хватает {closing - opening} открывающей скобки!")
else:
    print("Cкобки соответствуют!")