# listas entregadas
lista_1 = ['h','o','l','a','','m','u','n','d','o']
lista_2 = ['h','o','l','a','','l','u','n','a']
#lista nueva
lista_3 = []
# recorrer la lista
for item_1 in lista_1:
  #verificar si se repiten
  if item_1 in lista_2:
    #agregar a la lista nueva
    lista_3.append(item_1)
#mostrar los elementos de la nueva lista
for element in lista_3:
  print (element)