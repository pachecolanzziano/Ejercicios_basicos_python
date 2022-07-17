#Comprobar que el numero ingresado sea un numero entero sin convertirlo.
#Luis Carlos Pacheco Lanzziano
numero = input("ingrese un numero: ")
if ',' in numero:
    print("Seguramente es decimal", numero)
if '.' in numero:
    print("Seguramente es decimal", numero)
else:
    print("Seguramente es entero", numero)
    numero = int(numero)

print(type(numero))