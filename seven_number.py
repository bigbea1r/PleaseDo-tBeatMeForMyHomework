X = int(input("Введите число: "))
Y = int(input("Введите число: "))
sum =  0

for i in range(X, Y+1):
    if i % 5 == 0:
        sum = sum + i

print(sum)