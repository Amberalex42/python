# Указав номер четверти прямоугольной системы координат, показать
# допустимые значения координат для точек этой четверти.

n = int(input("Введите номер четверти: "))
if n == 1:
    print("Для этой четверти x > 0 и y > 0")
elif n == 2:
    print("Для этой четверти x < 0 и y > 0")
elif n == 3:
    print("Для этой четверти x < 0 и y < 0")
elif n == 4:
    print("Для этой четверти x > 0 и y < 0")
else:
    print("Такой четверти нет")