print("#2")
print("This dict have 4 people: Nikita Melgotchenko, David Shibru, Kamila Kamieva, Rysbek Tokoev")
a = input("Enter someone name and last name with underscore(_) for example: Nikita_Melgotchenko ")
d = dict(Nikita_Melgotchenko = "0.5", David_Shibru = "3.6", Kamila_Kamieva = "3.4", Rysbek_Tokoev = "3.6")
if a == "Nikita_Melgotchenko":
    print(d["Nikita_Melgotchenko"])
elif a == "David_Shibru":
    print(d["David_Shibru"])
elif a == "Kamila_Kamieva":
    print(d["Kamila_Kamieva"])
elif a == "Rysbek_Tokoev":
    print(d["Rysbek_Tokoev"])
else:
    print("You wrote something wrong, so try again!")