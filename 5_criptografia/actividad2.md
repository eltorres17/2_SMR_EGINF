
# Actividad: Creación de un algoritmo para ordenar una lista de mayor a menor

## Objetivo
Desarrollar un programa en Python que reciba una lista de números como entrada y devuelva la lista ordenada de mayor a menor. Los alumnos implementarán su propio algoritmo de ordenación.

---

## Instrucciones
1. Diseña un algoritmo para ordenar una lista de números de mayor a menor.
2. Implementa tu algoritmo en Python utilizando estructuras básicas como bucles y comparaciones.
3. Prueba tu programa con diferentes listas para asegurarte de que funciona correctamente.
4. Documenta tu código con comentarios explicativos para cada parte del algoritmo.

---

## Pistas
1. **Compara elementos:** Piensa en recorrer la lista y comparar cada elemento con el resto.
2. **Intercambia posiciones:** Si un elemento es menor que otro, intercámbialos de lugar.
3. **Usa bucles:** Utiliza un bucle para repetir el proceso hasta que toda la lista esté ordenada.
4. **Prueba con una lista pequeña:** Empieza con una lista sencilla, por ejemplo: `[3, 1, 4, 1, 5, 9]`.

---

## Consejos
- Un algoritmo básico que puedes implementar es **el método de burbuja**: recorre la lista varias veces, comparando e intercambiando elementos adyacentes si no están en el orden correcto.
- Piensa en cómo optimizar el proceso. ¿Es necesario recorrer toda la lista si ya está ordenada?

---

# Método de Burbuja

El **método de burbuja** es un algoritmo de ordenación simple que funciona comparando pares de elementos adyacentes en una lista y, si están en el orden incorrecto, los intercambia. Este proceso se repite hasta que la lista esté completamente ordenada.

---

## ¿Cómo funciona?
1. Comenzamos desde el primer elemento de la lista.
2. Comparamos el elemento actual con el siguiente:
   - Si el elemento actual es menor (o mayor, dependiendo del orden deseado) que el siguiente, los intercambiamos.
3. Continuamos este proceso para cada par adyacente de la lista.
4. Después de una pasada completa, el elemento más grande (o más pequeño) estará en su posición correcta al final de la lista.
5. Repetimos el proceso para los elementos restantes hasta que no se necesiten más intercambios.

---

## Ejemplo paso a paso
Queremos ordenar la lista `[5, 3, 8, 1]` de mayor a menor:

1. **Primera pasada:**
   - Comparar `5` y `3`: no intercambiar (5 es mayor que 3).
   - Comparar `3` y `8`: intercambiar → `[5, 8, 3, 1]`.
   - Comparar `3` y `1`: no intercambiar.

   Resultado después de la primera pasada: `[5, 8, 3, 1]`.

2. **Segunda pasada:**
   - Comparar `5` y `8`: intercambiar → `[8, 5, 3, 1]`.
   - Comparar `5` y `3`: no intercambiar.
   - Comparar `3` y `1`: no intercambiar.

   Resultado después de la segunda pasada: `[8, 5, 3, 1]`.

3. **Tercera pasada:**
   - Comparar `8` y `5`: no intercambiar.
   - Comparar `5` y `3`: no intercambiar.
   - Comparar `3` y `1`: no intercambiar.

   La lista ya está ordenada.

---

## Características del método de burbuja

### Ventajas
- Es fácil de entender e implementar.
- Útil para listas pequeñas o como ejercicio introductorio a los algoritmos de ordenación.

### Desventajas
- Es ineficiente para listas grandes (complejidad **O(n²)** en el peor caso).
- Realiza muchas comparaciones y movimientos incluso cuando la lista ya está casi ordenada.


