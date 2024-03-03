"""
Sokoban Game

Objetivo: Acomodar las cajas en un punto determinado
Elementos del juego:    0 - Personaje
                        1 - Cajas
                        2 - Metas
                        3 - Paredes
                        4 - Espacios/Piso
                        5 - Mapa
                     
*Niveles de juego (1 a Indeterminados)*

Reglas o mecánica del juego:
1. Empujar 1 caja (Hacia alguna dirección determinada en el piso).
2. Moverse hacia arriba sobre el piso.
3. Moverse hacia abajo sobre el piso.
4. Moverse hacia la izquiera sobre el piso.
5. Moverse hacia la derecha sobre el piso.
6. Reiniciar nivel.
7. Empujar 1 caja hacia arriba y que adelante este 1 piso.
8. Empujar 1 caja hacia abajo y que adelante este 1 piso.
9. Empujar 1 caja hacia la derecha y que adelante este 1 piso.
10. Empujar 1 caja hacia la izquierda y que adelante este 1 piso.
11. Cuando las cajas hayan sido colocadas en los puntos determiandos estas cambian de color.
12. Cuando todas las cajas hayan sido colocadas en los puntos determiandos el juego terminara y se avanzara un nivel.
"""

print("Welcome to the Sokoban Game")
player = input("Please, enter your player name: ")

mapa = [3, 4, 4, 0, 4, 4, 4, 3]

print(mapa)
personaje_col = 3

"""
a - izquierda
s - abajo
d - derecha
w - arriba
"""

movimientos = input(f"Presiona las teclas 'a' u 'd' para mover a {player}: ")

if movimientos == "a":
    mapa[2:4] = 0, 4
elif movimientos == "d":
    mapa[3:5] = 4, 0
else:
    print("Ingresa las letras solicitadas")

print(mapa)
    