#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24

def sum(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma

def multip(lista):
    multiplicar = 1
    for numero in lista:
        multiplicar = multiplicar * numero
    return multiplicar

def run():
    lista = [1, 2, 3, 4]
    print("Ël resultado de la suma de la lista es: "+str(sum(lista))+"\n y la multiplicacion de la lista es: "+str(multip(lista)))

    

if __name__ == "__main__":
    run()

