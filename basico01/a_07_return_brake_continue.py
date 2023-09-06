import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

# TODO: armazenar as URLs completas em uma lista
# TODO: deixar lista disponível para uma função chamada "extrair_infos" (a ser criada)
# TODO: acessar página através da função "acessar_página"
# TODO: printar os nomes de todos os títulos das 3 primeiras páginas das notas de imprensa

def acessar_pagina(url):
    página = requests.get(url)
    bs = BeautifulSoup(página.text, "html.parser")
    # print(bs)
    return bs

def extrair_infos():
    lista_de_links = construir_url()[0]
 #   print(lista_de_links)
    for link_geral in lista_de_links:
        print(link_geral)
        html = acessar_pagina(link_geral)
        #print(html)
        #<div id="content-core">
        conteudo = html.find('div', attrs={'id':'content-core'})
        lista_nota_imprensa = conteudo.find_all("article")
        for nota_de_imprensa in lista_nota_imprensa:
            titulo = nota_de_imprensa.h2.text.strip()
            link = nota_de_imprensa.a['href']
            numero = nota_de_imprensa.span.text
            lista_datas = nota_de_imprensa.find_all('span', attrs={'class':'summary-view-icon'})
            data = lista_datas[0].text.strip()
            horário = lista_datas[1].text.strip()
            print(titulo)
            print(link)
            print(numero)
            print(data)
            print(horário)
            print("###")


    # listaurls = tupla[0]
    # print(listaurls)
    # labri = tupla[1]
    # print(labri)

def construir_url():
    links_notasdeimprensa="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    contador = 360
    listaurls = []
    labri = 'artur'
    while contador >= 0:
        url_completa = links_notasdeimprensa + str(contador)
        if contador == 0:
            url_completa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
        contador = contador - 30
        # print(url_completa)
        listaurls.append(url_completa)
    #print(listaurls)
    return listaurls, labri

def main():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    # página_web = acessar_página(url)
    lista = extrair_infos()



if __name__ == "__main__":
    main()