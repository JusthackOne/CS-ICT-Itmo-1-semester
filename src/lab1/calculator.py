def check(t):
    t = t.replace(" ", "")
    for k in ["**", "-", "+", "/", "*"]:
        z = t.split(k)
        if len(z) == 2:
            break
    if len(z) < 2:
        print("Напишите строку в формате 2+2")
        return False

    for k in z:
        if k.isalpha() is True:
            print("Буквы не надо писать!")
            return False

    if z[-1] == "0" and "/" in t:
        print("На ноль делить нельзя!")
        return False
    return True

t = input()
if check(t) is True:
    print(eval(t))