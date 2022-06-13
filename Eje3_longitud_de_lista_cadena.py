#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
#Autor: Luis Carlos Pacheco Lanzziano
def calcular_longitud(palabra):
    i=0
    for n in palabra:
        i+=1
    return i

def run():
    palabra = str(input('Ingrese la palabra:'))
    print("La palabra tiene "+str(calcular_longitud(palabra))+" elementos")

if __name__ == "__main__":
    run()