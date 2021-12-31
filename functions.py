print("Functoins")
#functions it's a collection of instructions
#          it's a collection of code
def fun1():
    print("EZ")
    print("HARD")
print("It's outside the function")
fun1()
#a mapping
#input ore an return
def fun2(x):
    return 2*x
a = fun2(2)
#return valua or output
print(a)
def fun3(x,y):
    return x + y
a = fun3(2,4)
print(a)
def fun4(x):
    print(x)
    print("Still in this function")
    return 3*x
b = fun4(5)
print(b)
#BMI calculator
name1 = "YK"
height1_m = 2
weight1_kg = 80

name2 = "YK's dad"
height2_m = 1.9
weight2_kg = 90

name3 = "YK's bro"
height3_m = 1.8
weight3_kg = 85
def bmi_caclulator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m**2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + (" is not overweight")
    else:
        return name + (" is overweight")
result1 = bmi_caclulator(name1, height1_m, weight1_kg)
print(result1)
result2 = bmi_caclulator(name2, height2_m, weight2_kg)
print(result2)
result3 = bmi_caclulator(name3, height3_m, weight3_kg)
print(result3)