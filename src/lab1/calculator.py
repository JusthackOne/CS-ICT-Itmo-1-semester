# Проверки калькулятора
def check_calculator(text):
    t = t.replace(" ", "")
    for operation in ["**", "-", "+", "/", "*"]:    # Делаем список цифр
        dict_text = text.split(operation)
        if len(dict_text) == 2: # Проверям, есть ли у нас 2 числа
            break
    if len(dict_text) < 2:  # Проверям, есть ли у нас 2 числа
        print("Напишите строку в формате 2+2")
        return False

    for character in dict_text: # Проверям, есть ли буквы в переданной строке
        if character.isalpha() is True:
            print("Буквы не надо писать!")
            return False

    if dict_text[-1] == "0" and "/" in text: # Проверяем, является ли переданная строка делением на ноль
        print("На ноль делить нельзя!")
        return False
    return True

text = input()
if check_calculator(text) is True:
    print(eval(text))