#definir una funcion generar_n_carecteres() que tome un entero n y devuelva el caracter multiplicado por n. Ejemplo generar_n_carecteres(5, "x") deberia devolver "xxxxx"

def generar_n_carecteres(repeticiones, caracter):
    new_string = caracter*repeticiones
    return new_string

def run():
    print(generar_n_carecteres(10," \ 0 / "))

if __name__ == '__main__':
    run()