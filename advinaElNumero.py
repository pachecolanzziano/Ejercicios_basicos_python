# Adivina el numero
#Autor: Luis Carlos Pacheco Lanzziano

import random

numberRamdon = random.randint(1, 100)
intentos = 1
while(True):
  print('\n---==== Adivina el numero ====----')
  print(f'intento numero:{intentos}')
  numberPlayer = int(input('Cual numero crees que guardo? : '))
  if numberRamdon == numberPlayer:
    print(f'Felicitaciones el numero que escogí es el {numberRamdon}, lo haz adivinado.')
    break
  else:
    if numberRamdon > numberPlayer:
      print(f'Mnj cpu: mi numero es mayor que {numberPlayer}, sigue intentando')
      intentos += 1
    else:
      print(f'Mnj cpu: mi numero es menor que {numberPlayer}, sigue intentando')
      intentos += 1
      
    
