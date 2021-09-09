import requests
print(requests.__version__)

r = requests.get('http://google.com')

print(r) #r.content could've also been used but since the exact format of what should've been printed was not specified I just defaulted to this