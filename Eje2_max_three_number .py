#  Definir una función max() que tome como argumento tres números y devuelva el mayor de ellos.
def maximo(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        bigger_number = number1
    elif number2 > number1 and number2 > number3:
        bigger_number = number2
    else:
        bigger_number = number3
    return bigger_number

def run():
    number1 = int(input('Number 1:'))
    number2 = int(input('Number 2:'))
    number3 = int(input('Number 3:'))
    print("El numero mayor es: "+str(maximo(number1, number2,number3)))

if __name__ == "__main__":
    run()