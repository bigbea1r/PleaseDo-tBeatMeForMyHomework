input_str = input("Введите список чисел через запятую: ")

input_str = input_str.replace(" ", "")

numbers = input_str.split(",")

numbers.sort(reverse=True)

max_number = "".join(numbers)

print("Максимальное число:", max_number)