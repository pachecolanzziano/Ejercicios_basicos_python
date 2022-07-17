class cuentaNumeros(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
    

def numeros(cuenta):
  try:
    numeroCuenta = int(cuenta) #son numeros
    return True
  except ValueError:
    return False

def CantidadNumeros(cuenta):
  try:
    if len(cuenta)>9 or len(cuenta)<9: # son caractres
      raise cuentaNumeros('su numero de cuenta debe tener 9 digitos ')
    else:
      return True
  except cuentaNumeros as e:
      print(e.mensaje)

def run():
  nombre = input('Ingrese su nombre: ')
  cuenta = input('Ingrese su cuenta: ') 
  if numeros(cuenta):
    if CantidadNumeros(cuenta):
      print(f'usuario: {nombre} \n cuenta: {cuenta}')
  else:
    print('su cuenta no es valida')


if __name__ == '__main__':
    run()