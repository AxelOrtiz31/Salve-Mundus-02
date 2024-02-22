#Ejercicio de condiciones if, elif & else

a = 10
b = 9
c = 8

if a > b:
    print(a)
elif a > c:
    print(b)

if b > c:
     print(b)
else:
    print(c)

a = 7
b = 9
c = 5
d = 10

if a > b or a < c or d > c:
    print (a)
else: 
    print (c)

print("\n" * 0)


"""
Esto es un programa inicial para conocer las vocales
dentro de una palabra en especifica (MODE 01).
"""

cadena = "Hola mundo Python"

for caracter in cadena:
    print(caracter)

print("\n" * 0)

vocales = "aeiou"

contador_vocales = {i: cadena.lower().count(i) for i in vocales}

for i, x in contador_vocales.items():
    print(f"{i} : {x}")


print("\n" * 0)
print(cadena)
print("\n" * 0)



"""
Esto es un programa inicial para conocer las vocales
dentro de una palabra en especifica (MODE 02).
"""

palabra = input("Ingresa la palabra para conocer sus vocales: ")
vocals = "aeiou"

palabra_minus = palabra.lower()

print(palabra.find("o") * 2)

contador_vocales = {voc: palabra_minus.count(voc) for voc in vocals}

for v, n in contador_vocales.items():
    print(f"En la palabra {palabra} la vocal {v} se repite: {n} veces.")

print("\n" * 0)

"""
Esto es un programa inicial para conocer las vocales
dentro de una palabra en especifica (MODE 03).
"""

palabra = input("Ingresa la palabra para conocer sus vocales: ") #Se coloca una palabra
vocals_w = "aeiou" #Se definen las vocales en minuscula
vocals_p = "AEIOU" #Se definen las vocales en mayuscula

ortografia = palabra.capitalize() #Se corrige la palabra ingresada

print("\n" * 0) #Espacio
print(palabra.find("a")) #Busca un caracter en especifico
print("\n" * 0) #Espacio

contador_vocales_min = {voci: ortografia.count(voci) for voci in vocals_w} #Crea un metodo para contar las vocales en minusculas

contador_vocales_may = {vocy: ortografia.count(vocy) for vocy in vocals_p} #Crea un metodo para contar las vocales en mayusculas

for v, n in contador_vocales_min.items():
    print(f"En la palabra {ortografia} la vocal minúscula {v} se repite: {n} veces.")

print("\n" * 0) #Espacio

for w, p in contador_vocales_may.items():
    print(f"En la palabra {ortografia} la vocal mayúscula {w} se repite: {p} veces.")

print("\n" * 0) #Espacio

