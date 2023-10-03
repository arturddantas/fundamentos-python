import requests                                #Faz uma solicitação http
from bs4 import BeautifulSoup                  #Faz a análise html da página
from datetime import datetime, timedelta       #Analisa o intervalo como data



def acessar_pagina():
    url = 'https://www.gov.br/cultura/pt-br/assuntos/noticias'
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, 'html.parser')
    if pagina.status_code == 200:
        print(pagina.text)
        #return pagina

    elif pagina.status_code == 400:
        print(pagina)
        #return pagina
    return bs


def inserir_db():
    pass

def extrair_infos():
    pass
    #Fazer toda a análise do html nessa função

def construir_url():
    link = 'https://www.gov.br/cultura/pt-br/assuntos/noticias?b_start:int=' #Confirmar link
    contador = 600

    lista_de_links = []
    while contador >= 0:
        url_final = link + str(contador)
        if contador == 0:
            url_final = 'https://www.gov.br/cultura/pt-br/assuntos/noticias'
        contador = contador + 20
    lista_de_links.append(link)
    print(lista_de_links)



def salvar_internetarchive():
    pass

def gerar_html():
    pass



def main():
    final = url_principal()

if __name__ == "__main__":
    construir_url()

#https://www.gov.br/cultura/pt-br/assuntos/noticias
#https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias