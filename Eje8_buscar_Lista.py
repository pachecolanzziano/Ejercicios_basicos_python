# Definir una funcion superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en comun o devuelva False de lo contrario. Escribir la funcion usando el bucle for anidado.
#Autor: Luis Carlos Pacheco Lanzziano
def superposicion(lista1, lista2):
    for i in lista1:
        for k in lista2:
            if k == i:
                print('Este es el intruso: '+i)
                return True
    return False

def run():
    vocales = ['a','e','i','o','u']
    consonantes = ['w','t','h','y','u']
    if superposicion(vocales, consonantes):
        print ('Tienen un infiltrado')
    else:
        print('Todo en orden')

if __name__ == '__main__':
    run()