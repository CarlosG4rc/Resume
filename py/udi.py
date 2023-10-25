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

url_api1="https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/2023-10-11/"+hoy+"?token=04021aac739b77e232d9670147936836e9e9fc31e08bde26665c0f013df94471"

response = await pyfetch(url=url_api1, method="GET")

jsonsdatas1=await response.json()

jsonsdatas1=json.dumps(jsonsdatas1)

data1=json.loads(jsonsdatas1)

datahistoric=data1['bmx']['series'][0]['datos']

arr_data=np.array(datahistoric)

udi_value=np.array(1)
udi_date=np.array(1)

for i in arr_data:
    i=dict.items(i)
    arr=np.array(list(i))
    cadena=arr[1]
    cadena2=arr[0]
    udi_value=np.append(udi_value,cadena[-1])
    udi_date=np.append(udi_date,cadena2[-1])

udi_value=np.delete(udi_value,0)
udi_date=np.delete(udi_date,0)

fig, ax = plt.subplots()

ypoints = udi_value
xpoints = udi_date

plt.bar(xpoints,ypoints,align='center')

plt.xlabel('Date',fontsize=18)
plt.ylabel('Value',fontsize=18)
plt.title('UDI values')
plt.gcf().autofmt_xdate()

fig
pyscript.write('plot', fig)