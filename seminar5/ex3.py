# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = "Мама мыла рамуабв, рама мыабвла маму"
print(" ".join(filter(lambda x: "абв" not in x, text.split())))