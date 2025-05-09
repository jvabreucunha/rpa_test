import os
import pandas as pd

pasta_downloads = os.path.expanduser('~') + '\\Downloads'
nome_do_arquivo = 'challenge.xlsx'

caminho_arquivo = os.path.join(pasta_downloads, nome_do_arquivo)

def read(path):
    if os.path.exists(path):
        db = pd.read_excel(path)
        return db.to_dict(orient='records')
    else:
        return "file not found"

db = read(caminho_arquivo)
