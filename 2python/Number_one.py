elements = []

while True:
    input_value = input("Введите элемент: ")

    if input_value == "":
        break

    elements.append(input_value)

print("Итоговый список:")
for element in elements:
    print(element)