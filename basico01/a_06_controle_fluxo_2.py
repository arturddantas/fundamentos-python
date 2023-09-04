import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query


def main():
    construir_url()

def construir_url():
    links_notasdeimprensa="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    contador = 360
    while contador >= 0:
        url_completa = links_notasdeimprensa + str(contador)
        contador = contador - 30
        print(url_completa)


if __name__ == "__main__":
    main()

# Linha 14: redefinindo o valor da variável