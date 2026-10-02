
import numpy as np


# ================================================================
#  NIVEL 1 — Crear y manipular arrays
# ================================================================
#  Lo más básico: cómo crear arrays y hacer operaciones con ellos.
#  Un array de NumPy es como una lista de Python pero más rápido
#  y con operaciones matemáticas elemento a elemento.
# ================================================================

print("=" * 60)
print("NIVEL 1 — Crear y manipular arrays")
print("=" * 60)

# ---------------------------------------------------------------
#  1.1) Crea un array con las temperaturas de una semana:
#       [22, 25, 19, 30, 28, 21, 24]
#       Calcula la media, el máximo y el mínimo.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  1.2) Crea un array de alturas de 0 a 5000 metros, cada 500 m.
#       Usa np.arange.
#       ¿Cuántos elementos tiene?
# ---------------------------------------------------------------

# np.arange(inicio, fin, paso) — OJO: el fin NO se incluye,
# por eso ponemos 5500 si queremos que llegue a 5000.


# ---------------------------------------------------------------
#  1.3) Crea un array de 10 valores equidistantes entre 0 y 100.
#       Usa np.linspace.
# ---------------------------------------------------------------

# np.linspace(inicio, fin, cantidad) — aquí sí INCLUYE el fin.
# Es diferente de arange: le dices cuántos puntos quieres,
# no el paso.



# ---------------------------------------------------------------
#  1.4) Operaciones elemento a elemento.
#       Tienes temperaturas en Celsius: [0, 20, 37, 100]
#       Conviértelas a Fahrenheit:  F = C * 9/5 + 32
#       y a Kelvin:  K = C + 273.15
# ---------------------------------------------------------------

# En NumPy las operaciones se aplican a TODOS los elementos
# automáticamente. No necesitas un for loop.


# ---------------------------------------------------------------
#  1.5) Crea un array de 8 ceros y otro de 5 unos.
#       Usa np.zeros y np.ones.
# ---------------------------------------------------------------

# ================================================================
#  NIVEL 2 — Indexing y slicing
# ================================================================
#  Cómo seleccionar partes de un array.
#  Es igual que listas de Python pero con más poderes.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 2 — Indexing y slicing")
print("=" * 60)

# ---------------------------------------------------------------
#  2.1) Dado este array de presiones (hPa):
#       [1013, 950, 850, 700, 500, 300, 200, 100]
#       Obtén: el primer elemento, el último, los 3 primeros,
#       y los 3 últimos.
# ---------------------------------------------------------------

presion = np.array([1013, 950, 850, 700, 500, 300, 200, 100])

# ---------------------------------------------------------------
#  2.2) Del mismo array, obtén los elementos en posiciones pares
#       (0, 2, 4, 6) usando slicing con paso.
# ---------------------------------------------------------------

# array[inicio:fin:paso]


# ---------------------------------------------------------------
#  2.3) Modifica el array: cambia el valor en la posición 3
#       de 700 a 750. Luego cambia los dos últimos a 999.
# ---------------------------------------------------------------

presion_copia = presion.copy()   # hacemos copia para no perder el original

# ---------------------------------------------------------------
#  2.4) Tienes un array de 12 meses de lluvia (mm):
#       Obtén solo los meses de verano (junio=5, julio=6, agosto=7)
#       usando una lista de índices.
# ---------------------------------------------------------------

# "Fancy indexing": pasas una lista de índices y te devuelve
# los elementos en esas posiciones.

lluvia = np.array([30, 25, 40, 60, 80, 120, 150, 140, 90, 50, 35, 28])


# ================================================================
#  NIVEL 3 — Máscaras booleanas
# ================================================================
#  ESTE ES EL CONCEPTO MÁS IMPORTANTE para los ejercicios
#  de atmósfera. Una máscara es un array de True/False que
#  usas para filtrar datos.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 3 — Máscaras booleanas")
print("=" * 60)

# ---------------------------------------------------------------
#  3.1) Tienes temperaturas de 10 días:
#       Crea una máscara que sea True donde T > 25.
#       Úsala para obtener solo las temperaturas calientes.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  3.2) Combina condiciones: selecciona temperaturas entre 20 y 28
#       (inclusive). Usa & (and) con paréntesis.
# ---------------------------------------------------------------

# IMPORTANTE: cada condición va entre paréntesis cuando usas & o |
# & : and (ambas deben ser True)
# | : or  (al menos una debe ser True)
# ~ : not (invierte True/False)


# ---------------------------------------------------------------
#  3.3) ¿Cuántos días fueron calientes (T > 25)?
#       Usa np.sum sobre la máscara.
# ---------------------------------------------------------------

# True se cuenta como 1, False como 0.
# Entonces np.sum de una máscara = cantidad de True.


# ---------------------------------------------------------------
#  3.4) Reemplaza valores: pon 0 donde la temperatura sea menor
#       a 22 (simular que no hubo evento significativo).
# ---------------------------------------------------------------

# ---------------------------------------------------------------
#  3.5) Clasificación con máscaras: clasifica cada temperatura
#       como "fría" (<22), "templada" (22-28), o "caliente" (>28).
#       Cuenta cuántas hay de cada clase.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  3.6) np.where: encuentra los ÍNDICES donde se cumple una
#       condición. ¿En qué días (posiciones) llovió más de 80 mm?
# ---------------------------------------------------------------

lluvia = np.array([30, 25, 40, 60, 80, 120, 150, 140, 90, 50, 35, 28])

# np.where devuelve una TUPLA. El [0] saca el array de índices.
# ¿Por qué tupla? Porque en 2D devolvería (filas, columnas).
# En 1D solo hay un eje, pero la tupla siempre está.


# ================================================================
#  NIVEL 4 — Funciones útiles: diff, cumsum, nan
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 4 — diff, cumsum y NaN")
print("=" * 60)

# ---------------------------------------------------------------
#  4.1) np.diff: diferencias consecutivas.
#       Tienes alturas de un globo cada minuto:
#       [100, 250, 430, 600, 590, 610, 800]
#       Calcula cuánto subió (o bajó) entre cada minuto.
# ---------------------------------------------------------------

# np.diff calcula elemento[i+1] - elemento[i].
# Si hay N elementos, el resultado tiene N-1 elementos.

# ---------------------------------------------------------------
#  4.2) np.cumsum: suma acumulada.
#       Tienes lluvia horaria (mm): [2, 5, 0, 1, 8, 3, 0]
#       Calcula la lluvia acumulada a cada hora.
# ---------------------------------------------------------------

# cumsum: [2, 2+5, 2+5+0, 2+5+0+1, ...] = [2, 7, 7, 8, 16, 19, 19]


# ---------------------------------------------------------------
#  4.3) NaN: datos faltantes.
#       Tienes mediciones con huecos (sensor falló):
#       [22.5, nan, 23.1, 24.0, nan, nan, 22.8]
#       Calcula la media ignorando los NaN.
# ---------------------------------------------------------------

# np.nan es un valor especial = "no hay dato".
# np.mean falla con NaN (da NaN). Usa np.nanmean.



# ---------------------------------------------------------------
#  4.4) Detectar y contar NaN.
# ---------------------------------------------------------------



# ---------------------------------------------------------------
#  4.5) Reemplazar valores malos con NaN.
#       Un sensor marca -999 cuando falla. Límpialo.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
#  4.6) Limpieza combinada: reemplaza valores negativos Y
#       mayores a 100 con NaN (outliers de un sensor de humedad).
# ---------------------------------------------------------------

humedad = np.array([55, 72, -5, 88, 150, 63, -10, 91, 200, 45])

humedad_limpia = humedad.astype(float)  # necesario para poder poner NaN



# ================================================================
#  NIVEL 5 — Arrays 2D y operaciones por eje
# ================================================================
#  En meteorología casi siempre trabajas con datos 2D o más:
#  (estaciones × tiempo), (latitud × longitud), etc.
#  Entender los ejes es CLAVE.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 5 — Arrays 2D y ejes")
print("=" * 60)

# ---------------------------------------------------------------
#  5.1) Crea una matriz de temperaturas: 3 estaciones × 5 días.
#       Cada fila es una estación, cada columna es un día.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  5.2) Promedios por eje.
#       axis=0: promedia "hacia abajo" (sobre las estaciones)
#               → te da un promedio por día
#       axis=1: promedia "hacia la derecha" (sobre los días)
#               → te da un promedio por estación
# ---------------------------------------------------------------

# TRUCO para recordar: axis=X elimina esa dimensión.
#   axis=0 → elimina filas → queda un valor por columna
#   axis=1 → elimina columnas → queda un valor por fila



# ---------------------------------------------------------------
#  5.3) Máximo y mínimo por eje.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  5.4) Máscaras en 2D.
#       Encuentra todas las celdas donde T > 25.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  5.5) np.where en 2D.
#       Devuelve DOS arrays: filas y columnas.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  5.6) Seleccionar filas y columnas específicas.
# ---------------------------------------------------------------

# Una fila completa (estación B):

# Una columna completa (día 3):

# Un bloque (estaciones A y B, días 1 a 3):


# ================================================================
#  NIVEL 6 — Reshape y broadcasting
# ================================================================
#  Reshape cambia la forma de un array sin cambiar los datos.
#  Broadcasting permite operar arrays de distinto tamaño.
#  Ambos se usan MUCHO en datos atmosféricos.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 6 — Reshape y broadcasting")
print("=" * 60)

# ---------------------------------------------------------------
#  6.1) Reshape básico.
#       Tienes 24 mediciones horarias en un array 1D.
#       Reorganízalas en una matriz de 4 periodos × 6 horas.
# ---------------------------------------------------------------

# reshape no cambia los datos, solo la forma del array.
# El total de elementos debe coincidir: 24 = 4 × 6



# ---------------------------------------------------------------
#  6.2) Reshape para promedios por periodo.
#       Tienes 30 días × 24 horas = 720 datos de temperatura.
#       Calcula el promedio diario.
# ---------------------------------------------------------------

# Simulamos 720 horas de datos
np.random.seed(42)
temp_horaria = 20 + 5 * np.sin(2 * np.pi * np.tile(np.arange(24), 30) / 24) \
               + np.random.normal(0, 1, 720)

# Reshape a (30 días, 24 horas) y promediamos sobre las horas


# ---------------------------------------------------------------
#  6.3) Broadcasting: operaciones entre arrays de distinto tamaño.
#       NumPy "estira" el array más chico para que coincida.
# ---------------------------------------------------------------

# Ejemplo simple: restar la media de cada columna a una matriz.
# La matriz es (3, 5) y la media por columna es (5,).
# NumPy automáticamente resta cada media a su columna.



# ---------------------------------------------------------------
#  6.4) Broadcasting con None (np.newaxis).
#       A veces necesitas agregar un eje para que el broadcasting
#       funcione en la dirección correcta.
# ---------------------------------------------------------------

# Si quieres restar la media por FILA (no columna):

# Esto falla: datos(3,3) - media_fila(3,) resta por columna, no fila.
# Necesitas convertir media_fila de shape (3,) a shape (3, 1):




# ---------------------------------------------------------------
#  6.5) Ejemplo atmosférico: calcular anomalías mensuales.
#       Tienes 3 años × 12 meses de temperatura.
#       Calcula la climatología (promedio de cada mes) y resta.
# ---------------------------------------------------------------

# Simulamos datos: 3 años × 12 meses


# Climatología: promedio de cada mes sobre los 3 años

# Anomalías: cada año menos la climatología
# Broadcasting funciona directo: (3, 12) - (12,)


