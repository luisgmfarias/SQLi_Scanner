import requests #bib para requisições http
from IPython.display import HTML
import pandas as pd #bib para data science, estamos usando para ler o csv(comma separated values) 

sel_terms = pd.read_csv('dorks_terms.csv',usecols=[0]) #lendo csv

sel_terms = sel_terms.values.tolist() #transformando para tipo list

for item in sel_terms:
    search_term = ''.join(item) #join para selecionar texto

    print("\n BUSCA PELO TERMO:" + search_term ) #print para mostrar qual termo esta sendo buscado
    key = "3a88fbb112ec43b1bd0a7859b7181067" #key Azure da API do Bing
    assert key #verificação em tempo real

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search" #URL da API

    headers = {"Ocp-Apim-Subscription-Key" : key} #inserindo a Key na header
    params  = {"q": "instreamset:(url):" + search_term, "textDecorations":True, "textFormat":"HTML"} # passando o termo de busca como parametro para API
    response = requests.get(search_url, headers=headers, params=params) #realizando a busca
    response.raise_for_status() #verificando se request foi bem sucedido
    search_results = response.json() #retornando json dos resultados

    with open(r'results.txt', 'w') as f: #abrindo arquivo texto vazio de resultados
        for results in search_results["webPages"]["value"]: #laço para selecionar as url contidas no resultado JSON
            f.write(results["url"])
            f.write('#\n')#Separando cada URL por '#', isso se deve ao SQLmap quando vai ler uma lista de URLs em txt
        
