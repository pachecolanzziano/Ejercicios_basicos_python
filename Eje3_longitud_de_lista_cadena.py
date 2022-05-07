#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
def calcular_longitud(palabra):
    # i=0
    for i in palabra:
        i+=1
    return i

def run():
    palabra = input('Ingrese la palabra:')
    print("La palabra tiene "+str(calcular_longitud(palabra))+" elementos")

if __name__ == "__main__":
    run()