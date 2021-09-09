import requests
print(requests.__version__)

r = requests.get('https://raw.githubusercontent.com/Ayabdall/Lab1/master/lab1.py')

open('code.txt', 'wb').write(r.content)

x = open("code.txt", 'r').read()
print(x)