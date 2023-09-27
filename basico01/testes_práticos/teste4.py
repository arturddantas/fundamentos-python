import requests                                #Faz uma solicitação http
from bs4 import BeautifulSoup                  #Faz a análise html da página
from datetime import datetime, timedelta       #Analisa o intervalo como data



def url_principal():
    url = 'https://www.gov.br/cultura/pt-br/assuntos/noticias'
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    if pagina.status_code == 200:
        print(pagina)
        #return pagina

    elif pagina.status_code == 400:
        print(pagina)
        #return pagina


'''
def intervalo():
    for n in range(0, 10):
        data = datetime(2023, 9, 22) + timedelta(days=n)

O uso do datetime e timedelta talvez seja funcional apenas para quando quero definir um intervalo de coleta. Exemplo: quero coletar notícias
a cada 6 horas.
'''

def acessar_pagina():
    pass

def inserir_db():
    pass

def extrair_infos():
    pass

def construir_url():
    pass

def salvar_internetarchive():
    pass

def gerar_html():
    pass

def main():
    final = url_principal()

if __name__ == "__main__":
    url_principal()

#https://www.gov.br/cultura/pt-br/assuntos/noticias
#https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias