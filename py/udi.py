import json
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from pyodide.http import pyfetch
import asyncio

hoy=dt.date.today().strftime('%Y-%m-%d')

url_api="https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/"+hoy+"/"+hoy+"?token=04021aac739b77e232d9670147936836e9e9fc31e08bde26665c0f013df94471"


response = await pyfetch(url=url_api, method="GET")

jsonsdata=await response.json()

jsonsdata=json.dumps(jsonsdata)

data=json.loads(jsonsdata)

valor=data['bmx']['series'][0]['datos'][0]['dato']
fecha=data['bmx']['series'][0]['datos'][0]['fecha']

pyscript.write('udi', valor)
pyscript.write('fecha', fecha) 

url_api1="https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/2022-08-21/"+hoy+"?token=04021aac739b77e232d9670147936836e9e9fc31e08bde26665c0f013df94471"

response = await pyfetch(url=url_api1, method="GET")

jsonsdatas1=await response.json()

jsonsdatas1=json.dumps(jsonsdatas1)

data1=json.loads(jsonsdatas1)

datahistoric=data1['bmx']['series'][0]['datos']

arr_data=np.array(datahistoric)

udi_value=np.array

k=0

for i in arr_data:
    i=dict.items(i)
    deita=list(i)
    arr=np.array(deita)
    cadena=arr[1]
    # print(cadena[-1:])
    np.insert(udi_value,0,cadena[-1:])
    k=k+1

print(udi_value)