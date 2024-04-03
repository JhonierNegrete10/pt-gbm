def es_palindromo(word: str):
    word = word.lower().replace(" ", "")
    if len(word) < 2:
        return True
    if word[-1] == word[0]:
        return es_palindromo(word[1:-1])
    else:
        return False

def is_palindromo(word: str) -> bool:
    word = word.lower().replace(" ", "")
    return word == word[::-1]


if __name__ == "__main__":
   
    print("reconocer", is_palindromo("reconocer"))
    print("radar", is_palindromo("radar"))
    print("ojo", is_palindromo("ojo"))
    print("anilina", is_palindromo("anilina"))
    print("Anita lava la tina", is_palindromo("Anita lava la tina"))
    print("salas", is_palindromo("salas"))
    print("somos", is_palindromo("somos"))
    print("ese", is_palindromo("ese"))
    print("luego", is_palindromo("luego"))
