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

x = np.arange(0, 100, 10, dtype=float)

key = 0
key=int(key)
datos=np.array

for i in arr_data:
    np.insert(datos,float(i['dato']),key)
    key = key + 1
print(datos)

# print(datos)
# y = np.vstack([arr_data])

# fig, ax = plt.subplots()

# ax.set(xlim=(0, 100), xticks=np.arange(1, 100),
# ylim=(0, 100), yticks=np.arange(1, 100))

# ax.stackplot(x, y)

# plt.show()