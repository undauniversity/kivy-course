import requests, json

''' cara 1
r = requests.get(url='http://localhost/lat/api.php?auth=888&perintah=select')
#print(r.text)

isi = r.json()

print[isi]
'''

''' cara 2 '''
import urllib.request, json

with urllib.request.urlopen("http://localhost/lat/api.php?auth=888&perintah=select") as json_url:
    data = json.loads(json_url.read().decode())
    print(data)
    #print(json.dumps(data, indent=3, sort_keys=True))


''' cara 3
import requests

datos = requests.get("http://localhost/lat/api.php?auth=888&perintah=select").json
print(datos)
'''
