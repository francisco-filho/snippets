#!/usr/bin/env python3

from urllib.request import urlopen
import re

from bs4 import BeautifulSoup

# TODO A documentação do bs4 é bastante extensa é uma boa fonte de exemplos, 
# aqui iremos explicar apenas sobre 2 métodos que vão fazer todo o nosso trabalho
# `find_all` e `select`

def get_bs(url):
    html = urlopen(url)
    return BeautifulSoup(html, 'html.parser')

# Fazer scraping da página https://pt.wikipedia.org/wiki/Brasil
bs = get_bs("https://pt.wikipedia.org/wiki/Brasil")

# TODO explicar como visualizar os elementos html para scraping

# extrair links internos
def get_links_internos(bs):
    links = bs.select('#bodyContent a[href^="/wiki/"]')
    return links

# extrair enderecos das imagens
def get_endereco_imagens(bs):
    imgs = bs.select("#bodyContent")[0]\
        .find_all("img", {"src": re.compile("^//upload.wikimedia.*\.(jpg|jpeg|png|gif)$")})
    return imgs

# fazer o download das imagens
def baixar_imagens(bs):
    from urllib.parse import unquote
    from urllib.request import urlretrieve

    imagens = get_endereco_imagens(bs)[-10:]
    for img in imagens:
        nome = img['src'].rsplit('/', 1)[-1]
        img_url = f"https:{img['src']}"
        urlretrieve(img_url, unquote(nome))
        
# print lista de tags        
def print_tags(tags):
    for tag in tags:
        print (f"=> {tag}")


if __name__ == '__main__':
    baixar_imagens(bs)
