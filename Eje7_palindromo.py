#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def palindromo(palabra):
    inversa = palabra[::-1]
    return inversa

def run():
    palabra = input("ingrese la palabra:")
    palabra_inversa = palindromo(palabra)
    if palabra_inversa == palabra:
        print(palabra+"("+palabra_inversa+") es palindromo")
    else:
        print(palabra+"("+palabra_inversa+") NO es palindromo")


if __name__ == '__main__':
    run()