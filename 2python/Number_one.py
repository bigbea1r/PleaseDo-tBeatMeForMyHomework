elements = []

while True:
    input_value = input("Введите элемент: ")
    if not input_value:
        break
    elements.append(input_value)
print("Итоговый список:", elements)
