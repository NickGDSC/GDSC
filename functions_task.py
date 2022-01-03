print("fun_task")
def fun1(x, y):
    return x+y
def fun3(x, y):
    return x*y
def fun4(x, y):
    return x/y
def fun2(x, y):
    return x-y
a = []
b = int(0)
while b != 1:
    x = int(input("Введите любое число: "))
    y = int(input("Введите любое число: "))
    z = input("Выберите что сделать с числами(+,-,*,/): ")
    if z == "+":
        z = fun1(x,y)
        a.append(z)
        print(z)
        a = []
    elif z == "-":
        z = fun2(x,y)
        a.append(z)
        print(z)
        a = []
    elif z == "*":
        z = fun3(x,y)
        a.append(z)
        print(z)
        a = []
    elif z == "/":
        z = fun4(x,y)
        a.append(z)
        print(z)
        a = []
    c = input("Continue? Y/N: ")
    if c == "N":
        print("See you later!")
        b += 1