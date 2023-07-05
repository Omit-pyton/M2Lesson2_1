# Обробка винятків
# Обробіть виняток IndexError, коли програма намагається отримати доступ до неправильного індексу в списку.

try:
    my_list = [1, 2, 4, 57]
    my_choise = my_list[int(input("Enter your number: "))]
    print(my_choise)

except IndexError:
    print("Введено слишком большое значение")

