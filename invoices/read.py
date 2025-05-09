import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image
import os
import re
from datetime import datetime

# Configuração do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Configuração do WebDriver com User-Agent
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(options=options)

def extrac_date(texto):

    padrao_data = r"(\d{4}-\d{2}-\d{2}|[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})"
    resultado = re.search(padrao_data, texto)
    
    if resultado:
        data_encontrada = resultado.group(1).strip()
        try:
            # Se estiver no formato "YYYY-MM-DD"
            if re.match(r"\d{4}-\d{2}-\d{2}", data_encontrada):
                dt = datetime.strptime(data_encontrada, "%Y-%m-%d")
            else:
                # Tenta com mês abreviado; se falhar, tenta com mês por extenso
                try:
                    dt = datetime.strptime(data_encontrada, "%b %d, %Y")
                except ValueError:
                    dt = datetime.strptime(data_encontrada, "%B %d, %Y")
            return dt.strftime("%d-%m-%Y")
        except ValueError:
            return "Erro ao converter data"
    return "Data não encontrada"

def extrac_company(texto):

    padrao = r"(?s)(?:INVOICE\s*\n\s*#\s*\d+\s*\n\s*([A-Za-z0-9 &.,’'-]+)\s*\n\s*Date:)|(^[A-Za-z0-9 &.,’'-]+)\s+INVOICE"
    resultado = re.search(padrao, texto)
    if resultado:
        # Usa o grupo 1 se encontrado, senão o grupo 2
        empresa = resultado.group(1) if resultado.group(1) is not None else resultado.group(2)
        return empresa.strip()
    return "Nome da empresa não encontrado"

def extrac_invoice(texto):

    padrao = r"(?i)(?:Invoice\s*#|#\s*)(\d+)"
    match = re.search(padrao, texto)
    if match:
        return match.group(1)
    return "Invoice não encontrado"

def read(url):

    try:
        driver.get(url)

        # Aguarda até que a imagem esteja presente na página
        img_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "img"))
        )
        
        img_url = img_element.get_attribute("src")
        if not img_url:
            raise Exception("Erro ao capturar a URL da imagem.")

        file_name = img_url.split("/")[-1]

        # Baixa a imagem
        img_data = requests.get(img_url).content
        with open(file_name, "wb") as f:
            f.write(img_data)

        # Processa a imagem com OCR
        imagem = Image.open(file_name)
        texto = pytesseract.image_to_string(imagem, lang="eng")
        
        # Extração dos dados
        re_total = r"(?i)total[:\s]*\$?([\d,]+\.\d{2})"
        total_match = re.search(re_total, texto)
        total = total_match.group(1) if total_match else "Não encontrado"
        
        company = extrac_company(texto)
        date = extrac_date(texto)
        invoice_num = extrac_invoice(texto)

        # Remove o arquivo local
        os.remove(file_name)

        # Retorna os dados extraídos como um dicionário estruturado
        return {"Invoice": invoice_num, "Date": date, "Company": company, "Total": total}

    except Exception as e:
        return {"Erro": str(e)}


