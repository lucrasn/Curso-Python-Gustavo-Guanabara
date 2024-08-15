import requests


def verificar_acesso(url):
    try:
        acesso = requests.get(url)
        if acesso.status_code == 200:
            print(f'\033[1;32mO site {url} está acessível.\033[1m')
        else:
            print(f'\033[1;33mO site {url} está inacessível (status code: {acesso.status_code}).\033[m')
    except requests.exceptions.ConnectionError:
        print(f'\033[1;31mNão foi possível conectar-se ao site {url}. Verifique sua conexão com a internet.\033[m')


# URL para verificar
site = 'https://www.youtube.com'
# Chamada da função para verificar o acesso ao site
verificar_acesso(site)

# Guanabara
# import urllib.request
# try:
    # site = urllib.request.urlopen('http://www.pudincom.br')
# except urllib.error.URLError:
    # print('O site Pudim não está acessível no momento.')
# else:
    # print('Consegui acessar o site Pudim com sucesso!')
    # # Acessando o código HTML do site inteiro (extra)
    # print(site.read())
