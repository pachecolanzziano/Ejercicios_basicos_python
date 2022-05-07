#  Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
def maximo(number1, number2):
    if number1 > number2:
        bigger_number = number1
    else:
        bigger_number = number2
    return bigger_number

def run():
    number1 = int(input('Number 1:'))
    number2 = int(input('Number 2:'))
    print("El numero mayor es: "+str(maximo(number1, number2)))

if __name__ == "__main__":
    run()