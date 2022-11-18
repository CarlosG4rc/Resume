import json
import datetime as dt
hoy=dt.date.today().strftime('%Y-%m-%d')

url_api="https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/"+hoy+"/"+hoy+"?token=04021aac739b77e232d9670147936836e9e9fc31e08bde26665c0f013df94471"

from pyodide.http import pyfetch
import asyncio

response = await pyfetch(url=url_api, method="GET")

jsonsdata=await response.json()

jsonsdata=json.dumps(jsonsdata)

data=json.loads(jsonsdata)

valor=data['bmx']['series'][0]['datos'][0]['dato']
fecha=data['bmx']['series'][0]['datos'][0]['fecha']

pyscript.write('udi', valor) 
pyscript.write('fecha', fecha) 
