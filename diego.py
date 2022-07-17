# Importar librería
import requests
from bs4 import BeautifulSoup

url = "https://www.kavak.com/mx/comprar-Chevrolet/tipo-hatchback/precio-93182-min/compra-de-autos"

acceso_page = requests.get(url, timeout=5)

var_parseo = BeautifulSoup(acceso_page.content, "html.parser")


costes = var_parseo.find_all(class_="payment-total payment-highlight")
anio = var_parseo.find_all(class_="car-details")
modelos = var_parseo.find_all("h2", "car-name")
card = var_parseo.find_all("card-body")

# filtro por modelo
lista_modelos=[]
for item in modelos:
  modelo = item.text.replace(" ", "")
  modelo = item.text.replace('_ngcontent-sc267=""', "")
  modelo = item.text.replace(' class="car-name">', "")
  modelo = item.text.replace("car-name", "")
  if "sonic".upper() not in modelo.upper():
    lista_modelos.append(modelo)
    # print(modelo)
print(len(lista_modelos))

#filtro por costo
lista_coste = []
for item in costes:
    coste = item.text.replace(" ", "")
    coste = item.text.replace("<span _ngcontent-sc266=", "")
    coste = item.text.replace(",", "")
    coste = int(coste.replace("$",""))
    if  coste < 220000:
      lista_coste.append(coste)
      # print(coste)
print(len(lista_coste))








# card = var_parseo.find_all(class_="card-body")

# lista_web=[]
# for item in card:
#   coste2 = item.text.replace(" ", "")
#   coste2 = item.text.replace("<span _ngcontent-sc266=", "")
#   coste2 = item.text.replace("car-details", "")
#   coste2 = item.text.replace("car-name", "")
#   coste2 = item.text.replace(",", "")
#   coste2 = item.text.replace("•","")
#   coste2 = coste2.replace("$","")
#   if "Sonic" or "sonic" not in coste2:
#     if "2017" or "2018" or "2019" or "2020" or "2021" or "2022" or "2023" in coste2:
#       lista_web.append(coste2)

# for item in lista_web:
#   print(item)





# 
