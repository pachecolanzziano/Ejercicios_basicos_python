#Autor: Luis Carlos Pacheco Lanzziano

def leerDsv():
    data = []
    with open("./archivo.csv", "r", encoding="utf-8") as documento:
        for linea in documento:
            data.append(linea)
    documento.close()


def run():
    pass
if __name__ == "__main__":
    run()
