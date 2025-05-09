# main.py

from read import read
import pprint

for i in range(1, 12):
    url = f'https://rpachallengeocr.azurewebsites.net/invoices/{i}.jpg'
    dados = read(url)
    print('='*30)
    pprint.pprint(dados)

