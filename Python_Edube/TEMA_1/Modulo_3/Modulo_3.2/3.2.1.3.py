secret_number = 777
num = -1

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

while(num != secret_number):
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    num = int(input("Introduce un número: "))

print("¡Bien hecho, muggle! Eres libre ahora")

