import math

acc = int(-math.log10(float(input("Введите требуюмую точность от 0.1 до 0.0000000001: "))))
print(round(math.pi, acc))
