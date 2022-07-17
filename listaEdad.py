#se crea la lista ListaEdades
listaEdades = []
#un ciclo while true para poder preguntar varias veces si desea ingresar mas edades
while True:
    # se pide ingresar la la edad
    dato = input('Ingresa una edad: ')
    # se agrega la edad ingresada a la ultima pocicion de la lista gracias al metodo appedn
    listaEdades.append(dato)
    # pregunto si desea ingresar otra edad
    opcion = input('desea ingresar otra edad? Si / No: ')
    # pregunto si la opcion es no, el break lo que hace es romper el cilo while 
    if opcion.lower() == 'no': # lower() lo que hace es que el valor guardado en opcion pase a minuscula
        break
#lista las edades guardadas
for edad in listaEdades:
    print(edad)