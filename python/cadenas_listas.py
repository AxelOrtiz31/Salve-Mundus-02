name = ["Hello", "World", 322]

name[1:3] = 34, 54
print()
print(name)
print(name[0])
print()

for i in range(5):
    print(i)

print()

cadena = "dejah@gmail.com"

print(cadena[0],cadena[11],cadena[-1])
print()

for i in range(5, 14):
    print(cadena[i])
print()

for i in cadena:
    print(i)
print()

from random import randint

number = randint(4,5)

if number == 5:
    print("243")
else:
    print("Failed")
