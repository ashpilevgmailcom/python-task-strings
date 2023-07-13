def filter_strings(strings):
    """
    Фильтрует массив строк и возвращает новый массив, содержащий только строки, длина которых меньше или равна 3 символам.
    
    Аргументы:
    strings -- исходный массив строк
    
    Возвращает:
    Массив строк, удовлетворяющих условию фильтрации.
    """
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

# Ввод массива строк с клавиатура
strings = input("Введите строки, разделённые пробелом: ").split()

# Фильтрация строк
filtered_strings = filter_strings(strings)

# Вывод результата
print("Результат:", filtered_strings)