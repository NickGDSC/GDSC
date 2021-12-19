print("#1")
num = list(range(100, 0, -1))
for num in range(100, 0, -1):
    if num%7==0:
        print(num)

print("#2")
num = list(range(100))
for num in range(100, 0, -1):
    if num%4==0:
        print(num)

print("#3")
num = list(range(100, 0, -1))
for num in range(100, 0, -1):
    if num%13==0:
        print(num)
    elif num%8==0:
        print(num)

print("#4")

n = int(100)
while n>0:
    if (n*7+23)%2==0:
        print(n)
        n -= 1
    else:
        print("Я обязательно выживу")
        n -=1
        
#I was really happy when I did task #4