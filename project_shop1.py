def fun1(x, y):
    return x+y
def fun2(x, y):
    return x-y
item11 = int(2)
item12 = int(2)
item13 = int(2)
item14 = int(3)
item21 = int(3)
item22 = int(4)
item23 = int(2)
item24 = int(5)
item31 = int(3)
item32 = int(2)
item33 = int(4)
item34 = int(8)
item41 = int(4)
item42 = int(1)
item43 = int(2)
item44 = int(3)
PC = ["item11", "item12", "item13, item14"]
laptop = ["item21", "item22", "item23, item24"]
keyboard = ["item31", "item32", "item33", "item34"]
mouse = ["item41", "item42", "item43, item44"]
basket = []
x = int(0)
users = dict(Kuba="12345678")
admins = dict(Nick="nikita2003")
print("Login:")
login = input("Input your login: ")
if login in users:
    password = input("Input your password: ")
    if password == users[login]:
        print("Welcome",login)
    print("GDSC's shop")
    print("PC", "laptop", "keyboard", "mouse")
    while x != 1:
        a = input("Choose what you would like to buy: ")
        if a == "PC":
            print(PC)
            b = input("Сhoose which PC you want to buy: ")
            if b == "item11":
                print("quantity of good: ",
                      item11)  # I can add there something like n = int(input("choose how much would you like to buy: ))
                if item11 != 0:
                    basket.append("item11")
                    print("This item added to your basket")
                    item11 -= 1  # And this will look like item11 -= n  but it wasn't in task XD
                elif item11 == 0:
                    print("This item is absent")
                c = input("Would you like to buy something else? (Y/N): ")
                if c == "N":
                    x += 1
                    print(basket)
            elif b == "item12":
                print("quantity of good: ", item12)
                if item12 != 0:
                    basket.append("item12")
                    print("This item added to your basket")
                    item12 -= 1
                elif item12 == 0:
                    print("This item is absent")
                c = input("Would you like to buy something else? (Y/N): ")
                if c == "N":
                    x += 1
                    print(basket)
            elif b == "item13":
                print("quantity of good: ", item13)
                if item13 != 0:
                    basket.append("item13")
                    print("This item added to your basket")
                    item13 -= 1
                elif item13 == 0:
                    print("This item is absent")
                c = input("Would you like to buy something else? (Y/N): ")
                if c == "N":
                    x += 1
                    print(basket)
            elif b == "item14":
                print("quantity of good: ", item14)
                if item14 != 0:
                    basket.append("item14")
                    print("This item added to your basket")
                    item14 -= 1
                elif item14 == 0:
                    print("This item is absent")
                c = input("Would you like to buy something else? (Y/N): ")
                if c == "N":
                    x += 1
                    print(basket)
        elif a == "laptop":
            print(laptop)
            b = input("Сhoose which laptop you want to buy: ")
            if b == "item21":
                print("quantity of good: ", item21)
                if item21 != 0:
                    basket.append("item21")
                    print("This item added to your basket")
                    item21 -= 1
                elif item21 == 0:
                    print("This item is absent")
                c = input("Would you like to buy something else? (Y/N): ")
                if c == "N":
                    x += 1
                    print(basket)
            elif b == "item22":
                print("quantity of good: ", item22)
                basket.append("item22")
                print("This item added to your basket")
                item22 -= 1
            elif item22 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item23":
                print("quantity of good: ", item23)
                basket.append("item23")
                print("This item added to your basket")
                item23 -= 1
            elif item23 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item24":
                print("quantity of good: ", item24)
                basket.append("item24")
                print("This item added to your basket")
                item24 -= 1
            elif item24 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
        elif a == "keyboard":
            print(keyboard)
            b = input("Сhoose which keyboard you want to buy: ")
            if b == "item31":
                print("quantity of good: ", item31)
                basket.append("item31")
                print("This item added to your basket")
                item31 -= 1
            elif item31 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item32":
                print("quantity of good: ", item32)
                basket.append("item32")
                print("This item added to your basket")
                item32 -= 1
            elif item32 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item33":
                print("quantity of good: ", item33)
                basket.append("item33")
                print("This item added to your basket")
                item33 -= 1
            elif item33 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item34":
                print("quantity of good: ", item34)
                basket.append("item34")
                print("This item added to your basket")
                item34 -= 1
            elif item34 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
        elif a == "mouse":
            print(mouse)
            b = input("Сhoose which mouse you want to buy: ")
            if b == "item41":
                print("quantity of good: ", item41)
                basket.append("item41")
                print("This item added to your basket")
                item41 -= 1
            elif item41 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item42":
                print("quantity of good: ", item42)
                basket.append("item42")
                print("This item added to your basket")
                item42 -= 1
            elif item42 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item43":
                print("quantity of good: ", item43)
                basket.append("item43")
                print("This item added to your basket")
                item43 -= 1
            elif item43 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
            elif b == "item44":
                print("quantity of good: ", item44)
                basket.append("item44")
                print("This item added to your basket")
                item44 -= 1
            elif item44 == 0:
                print("This item is absent")
            c = input("Would you like to buy something else? (Y/N): ")
            if c == "N":
                x += 1
                print(basket)
    else:
        print("Wrong password")
elif login in admins:
    password = input("Input your password: ")
    if password == admins[login]:
        print("Welcome", login)
        while x != 1:
            a = input("Choose what you would like to add/del: ")
            if a == "PC":
                print(PC)
                b = input("Сhoose which PC you want to add/del: ")
                if b == "item11":
                    c = input("Would you like to (Add/Del)?: ")
                    if c == "Add":
                        item11 += 1
                    elif c == "Del":
                        item11 -= 1
                        d = input("Something else? (Y/N): ")
                        if c == "N":
                            x += 1
    else:
        print("Wrong password")
else:
    print("Wrong login")