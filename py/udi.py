# print('Hello World')
import requests
import json 

url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/2022-11-01/2022-11-02"

payload={}
headers = {}
parametres = {
    "token": "04021aac739b77e232d9670147936836e9e9fc31e08bde26665c0f013df94471"
}

response = requests.get(url, params=parametres)

text = json.dumps(response.text, sort_keys=True, indent=4)

print(text)
