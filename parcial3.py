#Autor: Luis Carlos Pacheco Lanzziano
import os

def run():
  while True:
    documentoUsuario = int(input("Digite documento del usuario: "))
    if documentoUsuario == 0:
      print('fin del programa')
      break
    nombreUsuario = input("Digite el nombre del usuario: ")
    telefonoUsuario = input("Digite el teléfono: ")
    while True:
      idServicio = input("Digite el identificador del servicio: ")
      if idServicio.upper() == "100A":
        cilindraje = 'Menos de 100 c.c'
        tipoMantenimiento = 'Inspección'
        descuento = '5%'
        total = 30000 - (30000 * 0.05)
        break
      elif idServicio.upper() == "101A":
        cilindraje = 'Menos de 100 c.c'
        tipoMantenimiento = 'Lubricación'
        descuento = '10%'
        total = 40000 - (40000 * 0.1)
        break
      elif idServicio.upper() == "102A":
        cilindraje = 'Menos de 100 c.c'
        tipoMantenimiento = 'Ajuste motor'
        descuento = '12%'
        total = 120000 - (120000 * 0.12)
        break
      elif idServicio.upper() == "103A":
        cilindraje = 'Menos de 100 c.c'
        tipoMantenimiento = 'Combo'
        descuento = '15%'
        total = 160000 - (160000 * 0.15)
        break
      elif idServicio.upper() == "100B":
        cilindraje = 'De 100 a 200 c.c'
        tipoMantenimiento = 'Inspección'
        descuento = '5%'
        total = 32000 - (32000 * 0.05)
        break
      elif idServicio.upper() == "101B":
        cilindraje = 'De 100 a 200 c.c'
        tipoMantenimiento = 'Lubricación'
        descuento = '10%'
        total = 40000 - (40000 * 0.1)
        break
      elif idServicio.upper() == "102B":
        cilindraje = 'De 100 a 200 c.c'
        tipoMantenimiento = 'Ajuste motor'
        descuento = '12%'
        total = 180000 - (180000 * 0.12)
        break
      elif idServicio.upper() == "103B":
        cilindraje = 'De 100 a 200 c.c'
        tipoMantenimiento = 'Combo'
        descuento = '15%'
        total = 210000 - (210000 * 0.15)
        break
      elif idServicio.upper() == "100C":
        cilindraje = 'De 200 o mas c.c'
        tipoMantenimiento = 'Inspección'
        descuento = '5%'
        total = 42000 - (42000 * 0.05)
        break
      elif idServicio.upper() == "101C":
        cilindraje = 'De 200 o mas c.c'
        tipoMantenimiento = 'Lubricación'
        descuento = '10%'
        total = 60000 - (60000 * 0.1)
        break
      elif idServicio.upper() == "102C":
        cilindraje = 'De 200 o mas c.c'
        tipoMantenimiento = 'Ajuste motor'
        descuento = '12%'
        total = 210000 - (210000 * 0.12)
        break
      elif idServicio.upper() == "103C":
        cilindraje = 'De 200 o mas c.c'
        tipoMantenimiento = 'Combo'
        descuento = '15%'
        total = 290000 - (290000 * 0.15)
        break
      else:
        print('El identificador de servicio ingresado no es valido\nintentalo de nuevo!')

    print('\nDatos del servicio')
    print(f'Documento del usuario: {documentoUsuario}')
    print(f'Nombre del usuario: {nombreUsuario}')
    print(f'Telefono: {telefonoUsuario}')
    print(f'Cilindraje: {cilindraje}')
    print(f'Tipo de mantenimiento: {tipoMantenimiento}')
    print(f'Porcentaje de descuento aplicado: {descuento}')
    print(f'Total a pagar: {total}\n')


if __name__ == "__main__":
  run()
