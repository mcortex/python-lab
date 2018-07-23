import requests
#HTTP GET:
r = requests.get('http://ip.jsontest.com/')
#Imprimo la salida
print("Response object:", r)
print("Response text:", r.text)

#GET con parametros

payload = {'q': 'mcortex'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL", r.url)
