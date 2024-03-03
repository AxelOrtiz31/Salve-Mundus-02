"""
Prueba #1
modificar_valor_lista

Esta prueba tiene la finalidad de lograr cambiar los valores que se encuentran
dentro de una lista para asi conseguir que el personaje, representado con el 
numero 0 logre cambiar de posición.
"""



mapa = [3,4,4,0,4,4,3]

#El personaje se movera a la derecha presionando la tecla 'd'
#El personaje se movera a la izquierda presionando la tecla 'a'

personaje_movimiento = str(input("Ingrese la tecla 'a' 'd' para mover al personaje a la izquierda u la derecha: "))

if personaje_movimiento == "a":
    mapa[2:4] = 0,4
    print(mapa)
elif personaje_movimiento == "d":
    mapa[3:5] = 4,0
    print(mapa)
else:
    print("Ingresa las letras solicitadas 'a''d'.")
