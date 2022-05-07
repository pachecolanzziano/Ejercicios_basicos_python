#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False
def verificar_vocal(caracter):
    if caracter =="a" or caracter =="e" or caracter =="i" or caracter =="o" or caracter =="u":
        vocal = True
    else:
        vocal = False
    return vocal

def run():
    caracter = str.lower(input('Escriba un caracter:'))
    print("vocal: "+str(verificar_vocal(caracter)))

if __name__ == "__main__":
    run()
