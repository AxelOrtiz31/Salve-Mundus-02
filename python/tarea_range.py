#Welcome
#Let´s start

cadena = "dejah@gmail.com"

for i in range (-15, 0, 2): #Establece un rango a tomar dentro de los valores de i, el primer numero dicta donde comienza, el segundo donde termina, y el tercero cuantos caracteres tomara en cuenta (Como una especie de salto).
    print(cadena[i])

print()
print()

for i in range (-14, 0, 2):
    print(cadena[i])

print()

for i in range (0, len(cadena), 2): #Similar, pero len es el que determina los valores a tomar, es decir el limite que en este caso por la variable cadena.
    print(cadena[i])

print()

for i in range (1, len(cadena), 2):
    print(cadena[i])

print()

for i in range (1):         #Christian
    print(cadena[0::2])

print()

for i in [0, 2, 4]:         #Jonathan
    print(cadena[i])

print()

for i in range (len(cadena)):
    if i % 2 != 0:          #Gael
        print(cadena[i])

print()

#End