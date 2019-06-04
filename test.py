import requests
from IPython.display import HTML
import pandas as pd
import csv

keep=range(4)
    
sel_terms = pd.read_csv('dorks_terms.csv', skiprows = lambda x: x not in keep, usecols=[0])

sel_terms = sel_terms.values.tolist()

for item in sel_terms:
    search_term = ''.join(item)

    print("\n BUSCA PELO TERMO:" + search_term )
    key = "496a09739cfb4310b63e8e69174aa850"
    assert key

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    headers = {"Ocp-Apim-Subscription-Key" : key}
    params  = {"q": "instreamset:(url):" + search_term, "textDecorations":True, "textFormat":"HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    with open(r'results.csv', 'w') as f:
        for results in search_results["webPages"]["value"]:
            f.write(results["url"])
            f.write(',\n')
        