import os, sys

def verificarArchivo():
  if(os.path.exists("alumno/alumno.txt")):
    return 'Abriendo archivo'
  else:
    os.mkdir("alumno")
    open("./alumno/alumno.txt", "a", encoding="utf-8")
    return 'Creando archivos...\nCarpeta y archivo creado ...'


def agregarAlumno():
  print(verificarArchivo())
  print('Registrar alumno')
  nombre = input("Nombre: ")
  edad = input("Edad: ")
  carrera = input("Carrera: ")
  promedio = input("Promedio: ")
  with open("./alumno/alumno.txt", "a", encoding="utf-8") as f:
    f.write(f"Nombre: {nombre} \nEdad: {edad} \nCarrera: {carrera} \nPromedio: {promedio}\n-------------------\n");
    f.close()

def verArchivo():
  with open("./alumno/alumno.txt", "r", encoding="utf-8") as f:
    for linea in f:
      print(linea.upper())
    f.close()
  

def run():
  while True:
    print('1) Ingresar información de estudiante')
    print('2) Mostrar alumnos registrados')
    print('3) Salir')
    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:
      agregarAlumno()
      os.system ("cls")
      print('Alumno registrado')

    elif opcion == 2:
      verArchivo()
    elif opcion == 3:
        print('Hasta luego.')
        break
    else:
        os.system ("cls")
        print(f'La opcion {opcion} no es valida, intentalo de nuevo')

if __name__ == '__main__':
  run()