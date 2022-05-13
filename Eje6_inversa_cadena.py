#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    #forma corta
    # return cadena[::-1] 
    inversa_cadena =""
    for caracter  in cadena:
        inversa_cadena = caracter + inversa_cadena
    return inversa_cadena

def run():
    cadena = input('ingresa tu cadena de texto: ')
    print("el resultado es: "+inversa(cadena))

if __name__ == '__main__':
    run()

