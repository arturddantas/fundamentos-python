def main():
    inserir="Brasil"
    lista(b=inserir)

def tupla():
    tupla = ('a', 'b', 'c', 'd')   #com parênteses ou não; recomendável usar parênteses
    x = tupla.count('c')  #conta quantos desse caracter específico tem na tupla
    y = tupla.index('d')  #posição do caracter na tupla
    if 'c' in tupla:
        print('"c" está na tupla')
    elif 'b' in tupla:   #não foi executado quando if verdadeiro; foi executado quando if falso. Dois 'ifs' são executados de qualquer forma, 'elif' é executado quando 'if' é falso.
            print('"b" está na tupla')
   # if not 'e' in tupla:
       # print('"e" não está na tupla')
    print('a' in tupla)  #True = existe na tupla. False = não existe na tupla
    print(tupla)
    print(x)
    print(y)

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
    tupla()

# len = contagem
# append = adicionar