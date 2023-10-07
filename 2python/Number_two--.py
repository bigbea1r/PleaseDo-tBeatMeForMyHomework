input_str = input("Введите список чисел через запятую: ")

numbers = input_str.split(",")

numbers = [num.strip() for num in numbers]

numbers.sort(reverse=True)

max_number = ''.join(numbers)

print("Максимальное число:", max_number)