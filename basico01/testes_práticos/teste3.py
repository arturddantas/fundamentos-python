import requests
from tinydb import TinyDB, Query
from datetime import datetime, timedelta

def inserir_db(data, url_pdf, categoria, num_edit, origem):
    db = TinyDB('teste.json', indent = 4, ensure_ascii = False)
    my_db = Query()
    verifica_db = db.contains(my_db.link_pdf == url_pdf)
    if not verifica_db:
        db.insert({
            'data': data,
            'origem': origem,
            'categoria': categoria,
            'num_edit': num_edit,
            'link_pdf': url_pdf,
        })

# https://www.franca.sp.gov.br/arquivos/diario-oficial/documentos/09-17042014.pdf

# Função para verificar a combinação e fazer a solicitação
def verifica_combinacao(url_completa_ordinária, url_completa_extraordinária):
    página = requests.get(url_completa_ordinária)
    página_extra = requests.get(url_completa_extraordinária)
    if (página.status_code == 200):
        print(página, url_completa_ordinária)
        categoria = 'ordinária'
        return página, categoria
 
    elif (página_extra.status_code == 200):
        print(página_extra, url_completa_extraordinária)
        categoria = 'extraordinária'
        return página_extra, categoria

    elif (página.status_code == 400):
        pass
    
    elif (página_extra.status_code == 400):
        pass

#{https://www.franca.sp.gov.br/arquivos/diario-oficial/documentos/}  {01} - {08042014} .pdf
def link_pdf(url):
    for edicao in range(1, 1000):
        for n in range(0, 10):  # 3458 é o número de dias de 08/04/2014 a 26/09/2023
            data = datetime(2014, 4, 8) + timedelta(days=n)
            url_completa_ordinária = f"{url}{edicao:02d}-{data.strftime('%d%m%Y')}.pdf"
            url_completa_extraordinária = f"{url}{edicao:02d}-Extra-{data.strftime('%d%m%Y')}.pdf"
            url_pdf = verifica_combinacao(url_completa_ordinária, url_completa_extraordinária)[0]
            if type(url_pdf) == tuple():
                categoria = url_pdf[1]
                num_edit = edição
                origem = 'Franca' 
                banco = inserir_db(data, url_pdf, categoria, num_edit, origem)


def main():
    url = 'https://www.franca.sp.gov.br/arquivos/diario-oficial/documentos/'
    link_pdf(url)

if __name__ == "__main__":
    main()