# Webscraping a Wikipedia

## Webscraping

Webscraping é a atividade de localizar e capturar conteudosd de sites por meio de processos automatizados (robôs). 

Os programas que fazem webscraping tambem são conhecidos com `web crawlers` (rastreadores da web), eles vasculham toda a web capturando informações e geralmente guardam essa informação em banco de dados. Podemos dizer que o web crawler mais famoso é o google, que varre toda a web e disponibiliza todo o conteudo acumulado através da sua pesquisa (e propagandas).

Veremos aqui como criar um web crawler em python, é um processo razoavelmente simples para o tamanho das possibilidades de dados que ele te coloca nas mãos.

### O que deve saber para criar um webcrawler

Bem, o crawler irá capturar páginas da internet para que você consiga extrair algum conteudo. Como as páginas são criadas principalmente em HTML e CSS, o conhecimento básico destas duas tecnologias é necessário. Conhecer o html te ajudará no momento de localizar quais partes das páginas você quer capturar, já que não é interessante capturar propagandas e outros conteudos indesejados. O conhecimento de CSS tambem vai ajudar, pois é a forma mais simples de selecionar elementos dentro de uma página HTML.

Tambem precisamos de conhecimento em alguma linguagem de programação, o exemplo aqui descrito é feito em `python` quem possui bibliotecas prontas que facilitam muito o nosso trabalho.

## Preparando ambiente

Utilizaremos duas bibliotecas do python para criar a nossa ferramento da captura:

- `urllib` que faz parte da biblioteca padrão do python
- `BeaultifulSoup4` que utilizaremos para navegar entre os elementos do html

### Instalação

Para installar o beaultifulSoup execute o seguinte commando no terminal `pip install beaultifulsoup4`

## Scraping
### Lendo artigo, titulo e conteudo, links

A [documentação do beautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) é bastante extensa é uma boa fonte de exemplos, mas aqui iremos trabalhar apenas com  2 métodos que vão fazer todo  nosso trabalho
- `find_all(name, attrs)` nos permite localizar um elemento passando o nome e atributos do mesmo
- `select(css_selector)` com o select podemos localizar elmentos passando seletores css, ótimo para quem já utilizou jQuery 

Antes de começarmos a escrever a primeira linha de código devemos abrir a página que queremos capturar e visualizar seus elementenos, tentar identificar padrões para que possamos criar o scrapper da forma mais confiável possível, no caso da `wikipedia`, verificamos que o conteúdo principal está dentro de uma `div#bodyContent` e podemos identifica-los facilmente inspecionando a página no navegador.


## Aspectos Legais

Este é um artigo sobre a implentação de um webcrawler, mas deixo claro aqui que é importante entender o que pode e não pode ser feito no que diz respeito a captura de dados automatizada na web. Para entender um pouco mais sobre esse assunto veja o artigo [Coleta de dados](https://pt.wikipedia.org/wiki/Coleta_de_dados_web), e na dúvida **consulte um advogado :D**.


## Robots.txt

O arquivo `robots.txt` é uma forma que os sites tem de informar aos web crawlers quais conteudos/url's dentro do site são permitidas ou proibidas de serem visualizadas. Esse arquivo é apenas uma recomendação já que os sites não tem como impedir que os crawlers acessem seus conteúdos públicos, mas acredito que se o site nos dá informação útil e de maneira livre não custa nada respeitarmos usas recomendações.

O arquivo `robots.txt` é simplesmente um arquivo texto com informações dos chamados `agents` que nada mais é do que os robos, navegadores, ferramentas que acessam o site de maneira automatizada ou não, e as regras de liberação `allow` e proibição `disallow` de acesso pelo agente. Caso você criar um crawler é interessante ler o artigo [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard) na wikipedia.

Se está curioso e quer ver um arquivo `robots.txt` basta digitar o site que você deseja capturar e abrir diretamente o arquivo no browser:

Exemplo: digite na barra de endereços `https://www.cnnbrasil.com.br/robots.txt` e será aberto as configurações para o site da [CNN Brasil](https://www.cnnbrasil.com.br/).


## Referência

- [Coleta de dados](https://pt.wikipedia.org/wiki/Coleta_de_dados_web)
- [Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)