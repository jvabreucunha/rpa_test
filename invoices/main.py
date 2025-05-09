from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from read import read
import time

import pprint

# Inicializa o WebDriver
service = Service(ChromeDriverManager().install())  
driver = webdriver.Chrome(service=service)  
driver.get('https://rpachallengeocr.azurewebsites.net/')

# Inicia o desafio
start = driver.find_element(By.ID, 'start')
start.click()

data_to_excel = []

for i in range(0, 3):
    time.sleep(2)

    tabela = driver.find_element(By.TAG_NAME, 'table')
    linhas = tabela.find_elements(By.TAG_NAME, 'tr')

    for j, linha in enumerate(linhas):
        colunas = linha.find_elements(By.TAG_NAME, 'td')
        line_excel = {}
        
        for index, coluna in enumerate(colunas):
            if index == 1:
                line_excel['id'] = coluna.text  # Use chave em vez de atributo
            elif index == 2:
                line_excel['DueDate'] = coluna.text  # Use chave em vez de atributo
            elif index == 3:
                link = coluna.find_element(By.TAG_NAME, 'a')
                url_pagina = link.get_attribute("href")
                print("URL capturada:", url_pagina, '\n')  # Depuração

                data_img = read(url_pagina)
                line_excel['invoiceNo'] = data_img.get('Invoice', 'Não encontrado')  
                line_excel['InvoiceDate'] = data_img.get('Date', 'Não encontrado')  
                line_excel['CompanyName'] = data_img.get('Company', 'Não encontrado')  
                line_excel['TotalDue'] = data_img.get('Total', 'Não encontrado')
                data_to_excel.append(line_excel)  
    if i < 2:
        next = driver.find_element(By.ID, 'tableSandbox_next')
        
        driver.execute_script("arguments[0].scrollIntoView(true);", next)
        driver.execute_script("arguments[0].click();", next)
    else:
        df = pd.DataFrame(data_to_excel)
        df.to_excel('invoices.xlsx', index=False, engine='openpyxl')
        file_input = driver.find_element(By.NAME, 'csv')
        file_input.send_keys(r"C:\0 - prog\Python\RPA\RPA_TEST\invoices\invoices.xlsx")
        time.sleep(10)

pprint.pprint(data_to_excel)
driver.quit()
