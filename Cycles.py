print("Lesson")
n = 1000
while n > 100:
    print(n)
    n /= 2

for i in "Hello world":
    print(i * 2)

for i in "Hello world":
    print(i * 2, end = "")

for i in "Hello world":
    if i == "w":
        continue
    print(i * 2, end = "")

for i in "Hello world":
    if i == "w":
        break
    print(i * 2, end = "")

for i in "Hello world":
    if i == "a":
        break
    print(i * 2)
else:
    print("Буквы а нету в слове")

a = list(range(1,11))
print(a)
total = 0
for v in range(1,11):
    total = total + v
print(total)

print("Task")
print("#1")
i = list(range(100, 0, -2))
print(i)
print("#2")
for i in range(100, 0, -2):
    if i%2==0:
        print(i)

print("#3")
a = (100)
while a>0:
    if a%2!=0:
        print(a)
        a -=1
    else:
        print("Четное число")
        a -=1