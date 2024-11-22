"""def calcular_promedio(notas):
    return sum(notas) / len(notas)

notas = [8, 9, 7, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio:.2f}")
"""
"""
def es_color_primario(color):
    colores_primarios = ["rojo", "azul", "amarillo"]
    color = color.lower()
    if color in colores_primarios:
        print(f"El color {color.capitalize()} es primario")
    else:
        print(f"El color {color.capitalize()} no es primario")
color = input("Ingrese un color: ")
es_color_primario(color)
"""

"""
def encontrar_mayor(*numeros):
    
    if not numeros:
        raise ValueError("No se proporcionaron números")

    mayor = max(numeros)
    print(f"El número mayor es: {mayor}")
    return mayor

# Ejemplo de uso:
encontrar_mayor(10, 20, 30, 60, 50)

"""
"""
def dibujar_rectangulo(filas, columnas):
   
    for i in range(filas):
        for j in range(columnas):
            if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Ejemplo de uso:
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
dibujar_rectangulo(filas, columnas)
"""
def calcular_factorial(n):
    
    if n < 0:
        raise ValueError("El número debe ser entero positivo")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Ejemplo de uso:
n = int(input("Ingrese un número entero positivo: "))
print(f"El factorial de {n} es: {calcular_factorial(n)}")

