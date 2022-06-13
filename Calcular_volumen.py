#  Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
#Autor: Luis Carlos Pacheco Lanzziano
def volumen(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    return volumen

def run():
    alto = float(input("ingrese alto: "))
    ancho = float(input("ingrese ancho: "))
    profundo = float(input("ingrese profundo: "))
    print ("El volumen es: "+str(volumen(alto, ancho, profundo)))

if __name__ == "__main__":
    run()