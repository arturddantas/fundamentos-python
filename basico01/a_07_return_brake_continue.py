import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

# TODO: armazenar as URLs completas em uma lista
# TODO: deixar lista disponível para uma função chamada "extrair_infos" (a ser criada)
# TODO: acessar página através da função "acessar_página"
# TODO: printar os nomes de todos os títulos das 3 primeiras páginas das notas de imprensa

def acessar_página(url):
    página = requests.get(url)
    bs = BeautifulSoup(página.text, "html.parser")
    # print(bs)
    return bs

def construir_url():
    links_notasdeimprensa="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    contador = 360
    listaurls = []
    while contador >= 0:
        url_completa = links_notasdeimprensa + str(contador)
        if contador == 0:
            url_completa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
        contador = contador - 30
        # print(url_completa)
        listaurls.append(url_completa)
    return listaurls
    print(listaurls)

def main():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    # página_web = acessar_página(url)
    lista_urls = construir_url()
    print(lista_urls)


if __name__ == "__main__":
    main()

