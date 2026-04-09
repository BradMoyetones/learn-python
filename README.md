# Nivel Básico - Consolidación de Sintaxis

1.  **Manipulación de Listas (List Comprehension):**
    Dada una lista de números del 1 al 50, genera una nueva lista que contenga solo los cuadrados de los números que son divisibles por 3. Intenta hacerlo en una sola línea de código.

2.  **Frecuencia de Caracteres:**
    Escribe una función que reciba un string y devuelva un diccionario donde las llaves sean los caracteres y los valores sean la cantidad de veces que aparecen. (Ignora espacios y mayúsculas).

3.  **Filtrado de Diccionarios:**
    Tienes un diccionario con nombres de productos como llaves y sus precios como valores. Crea una función que reciba este diccionario y un presupuesto máximo, y devuelva un nuevo diccionario solo con los productos que puedes costear.

4.  **Generador de Contraseñas Simple:**
    Crea un script que genere una contraseña aleatoria combinando letras mayúsculas, minúsculas, números y un set específico de caracteres especiales, usando el módulo `random`.

5.  **Validación de Palíndromos:**
    Escribe una función que determine si una frase es un palíndromo (se lee igual de atrás hacia adelante), ignorando espacios, tildes y signos de puntuación.

---

# Nivel Intermedio - Lógica y Estructura

6.  **Manejo de Errores y Archivos:**
    Escribe un programa que intente leer un archivo de texto. Si el archivo no existe, debe capturar la excepción, crear el archivo con un texto por defecto y luego imprimir el contenido.

7.  **Decorador de Tiempo:**
    Crea un **decorador** llamado `@medir_tiempo` que, al aplicarse a cualquier función, imprima en consola cuánto tiempo tardó esa función en ejecutarse (puedes usar el módulo `time`).

8.  **Programación Orientada a Objetos (Dunder Methods):**
    Crea una clase `Producto` con atributos `nombre` y `precio`. Implementa el método especial `__str__` para que al imprimir el objeto se vea como "Producto: [Nombre] - $[Precio]" y el método `__gt__` para poder comparar dos productos por su precio usando el operador `>`.

9.  **Generadores para Memoria Eficiente:**
    Escribe una función generadora (usando `yield`) que devuelva la secuencia de Fibonacci hasta un número $N$ dado. Esto es útil para entender cómo manejar grandes volúmenes de datos sin saturar la RAM.

10. **Agrupación de Datos (Tip: `itertools` o `collections`):**
    Dada una lista de tuplas que representan ventas `(fecha, producto, monto)`, escribe una lógica que agrupe y sume el total de ventas por cada producto.
