import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def acessar_página(url):
    página = requests.get(url)
    bs = BeautifulSoup(página.text, "html.parser")
    # print(bs)
    return bs

def construir_url():
    links_notasdeimprensa="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    contador = 360
    while contador >= 0:
        url_completa = links_notasdeimprensa + str(contador)
        if contador == 0:
            url_completa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
        contador = contador - 30
        print(url_completa)

def main():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    # página_web = acessar_página(url)
    lista_urls = construir_url()


if __name__ == "__main__":
    main()

