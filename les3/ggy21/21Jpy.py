x = float(input(4.82))
y = float(input(24.21))
z = 2.0
s = 14

print(x * 2 + y / 4 + z + s * 2.5)

fruit = input("Введите название фрукта: ")
message = f"{fruit} - самый вкусный во всем мире!"
print(message)
print("Длина названия фрукта:", len(fruit))




perimeter = float(input("Введите периметр треугольника: "))
x = float(input("Введите основание треугольника: "))

a = (perimeter - 2 * x) / 2
b = x / 2

print("Сторона  a:",  a)
print("Сторона  b:",  b)





number = int(input("Введите число: "))

if 10 <= number <= 20:
    print(True)
else:
    print(False)
