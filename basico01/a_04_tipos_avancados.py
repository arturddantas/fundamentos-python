def main():
    inserir="Brasil"
    lista(b=inserir)

def lista(b,a="Argentina"):
    lista=[]
    print(b)
    print(lista)
    lista.append(a)
    print(type(lista))
    print(lista)
    print(len(lista))
    lista.append("Uruguai")
    print(lista)
    print(len(lista[1]))

def conjunto():
    conjunto={"Brasil", "Argentina"}
    print(conjunto)

def dicionário():
    dicionário={
        "país":"Brasil", 
        "continente":"América"}
    print(dicionário["país"])
    print("país" in dicionário)



if __name__ == "__main__":
    dicionário()

# len = contagem
# append = adicionar