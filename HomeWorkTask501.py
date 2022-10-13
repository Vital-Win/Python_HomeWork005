# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {my_text}")
my_text = del_some_words(my_text)
print(my_text)
