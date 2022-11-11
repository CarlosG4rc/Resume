# print('Hello World')
import requests
import json 

url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/2022-11-01/2022-11-02 displa "

payload={}
headers = {}

response = requests.get(url,verify=False)

text = json.dumps(response.text, sort_keys=True, indent=4)
print(text)

print(text)