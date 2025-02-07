### Sección 1: Introducción
# Introducción
# Este notebook explora el uso de funciones en Python, su importancia en la programación modular y su impacto en la eficiencia del código.

"""
Las funciones en Python son bloques de código reutilizables que permiten estructurar programas de manera modular.
Su uso contribuye a la claridad, mantenimiento y eficiencia del código.
"""

### Sección 2: Investigación y Ejemplos
## 3.1 Definición y Propósito de las Funciones en Python

"""
¿Qué son las funciones?
Las funciones en Python permiten encapsular código reutilizable, mejorando la modularización y eficiencia en el desarrollo de software.

Beneficios de modularizar código con funciones:
- Reutilización del código.
- Reducción de errores.
- Facilidad de mantenimiento.
- Claridad y organización.
"""

# Ejemplo de una función simple en Python
def saludar():
    print("¡Hola, bienvenido a Python!")

saludar()

## 3.2 Tipos de Funciones en Python

# 1. Función con y sin retorno
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("Resultado de la suma:", resultado)

# 2. Funciones con parámetros y valores predeterminados
def presentar(nombre, edad=25):
    print(f"Nombre: {nombre}, Edad: {edad}")

presentar("Carlos")

# 3. Uso de *args y **kwargs
def suma_multiple(*args):
    return sum(args)

print("Suma de múltiples valores:", suma_multiple(1, 2, 3, 4, 5))

# 4. Funciones anónimas (lambda)
cuadrado = lambda x: x ** 2
print("Cuadrado de 4:", cuadrado(4))

# 5. Funciones recursivas
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial de 5:", factorial(5))

# 6. Generadores (yield)
def generador():
    for i in range(3):
        yield i

for num in generador():
    print("Generador produce:", num)

# 7. Closures y decoradores
def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

doble = crear_multiplicador(2)
print("Doble de 4:", doble(4))

## 3.3 Aplicación de Funciones en Problemas Reales

# 1. Aplicación en estructuras de datos
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

print("Lista filtrada:", filtrar_pares([1, 2, 3, 4, 5, 6]))

# 2. Uso de funciones en procesamiento de datos
def convertir_mayusculas(lista_palabras):
    return list(map(str.upper, lista_palabras))

print("Lista en mayúsculas:", convertir_mayusculas(["hola", "mundo"]))

# 3. Optimización del rendimiento con funciones
def suma_rapida(lista):
    return sum(lista)

print("Suma optimizada:", suma_rapida(range(1000000)))

# 4. Comparación entre funciones definidas por el usuario y funciones integradas
print("Longitud de una lista con len():", len([1, 2, 3, 4, 5]))

def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

print("Longitud de una lista con función personalizada:", contar_elementos([1, 2, 3, 4, 5]))

### Sección 3: Conclusiones
"""
Resumen de hallazgos:
- Las funciones en Python permiten escribir código modular y reutilizable.
- Existen distintos tipos de funciones según su uso y comportamiento.
- Aplicarlas correctamente mejora la eficiencia y claridad del código.

Análisis personal:
El uso de funciones es esencial para cualquier programador, ya que ayuda a estructurar el código de manera ordenada y comprensible.
"""

# Referencias
"""
- Documentación oficial de Python: https://docs.python.org/3/tutorial/
- Libros recomendados: "Python Crash Course" de Eric Matthes
"""
