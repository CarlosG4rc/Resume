import http.client

conn = http.client.HTTPConnection("www.banxico.org.mx")
payload = ''
headers = {}
conn.request("GET", "/SieAPIRest/service/v1/series/SP68257/datos?token=04021aac739b77e232d9670147936836e9e9fc31e08bde26665c0f013df94471", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))