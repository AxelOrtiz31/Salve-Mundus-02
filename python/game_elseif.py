"""
Bienvendio a este programa de prueba
Espero te guste
Tratare de leerte la fortuna
"""

#Let's begin!

import random
number = random.randint(1,8)

for i in range(3):
    print("¡Empecemos!")

name = input("Ingresa tu nombre para comenzar: ")

print("Tu suerte el dia de mañana sera la siguiente: ")

if number == 1:
    print("TE MORDERA UN PERRO")
elif number == 2:
    print("SERA MEJOR QUE REVISES TU BILLETERA")
elif number == 3:
    print("MEJOR QUE AYER")
elif number == 4:
    print("MEJOR YA NI LA MUELES")
elif number == 5:
    print("TRY AGAIN")
elif number == 6:
    print("TE ENCONTRAS UN BILLETE DE 500 PESOS")
elif number == 7:
    print("TU AMOR APARECERA")
else:
    print("Ya fuiste...")
