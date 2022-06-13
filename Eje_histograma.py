# Definir un histograma procedimiento() que tome una lista de numeros enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento ([4, 9, 7]) deberia imprimir lo siguiente:
# **** 
# **** 
# **** 
#Autor: Luis Carlos Pacheco Lanzziano
def letra_A():
    print('''********
********
**    **
********
********
**    **
**    **''') 

def procedimiento(lista):
    for numero in lista:
        print("*"*numero)

def run():
    # procedimiento([35,35,35,35,35,])
    letra_A()
if __name__ == '__main__':
    run()