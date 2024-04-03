import timeit

from main import es_palindromo, is_palindromo

# Palabra de prueba
word = "Anita lava la tina"

# Benchmark para la función es_palindromo
time_es_palindromo = timeit.timeit(lambda: es_palindromo(word), number=10000)

# Benchmark para la función is_palindromo
time_is_palindromo = timeit.timeit(lambda: is_palindromo(word), number=10000)

print(f"Tiempo de ejecución para es_palindromo: {time_es_palindromo} segundos")
print(f"Tiempo de ejecución para is_palindromo: {time_is_palindromo} segundos")
