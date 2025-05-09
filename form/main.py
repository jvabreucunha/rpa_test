from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from dados import read, caminho_arquivo
import time

db = read(caminho_arquivo)

service = Service(ChromeDriverManager().install())  #
driver = webdriver.Chrome(service=service)  

driver.get('https://www.rpachallenge.com/')
driver.implicitly_wait(10) 

start = driver.find_element(By.XPATH, "//button[text()='Start']")
start.click()

for line in db:
    inputCompanyName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]')
    inputCompanyName.send_keys(line['Company Name'])

    inputEmail = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]')
    inputEmail.send_keys(line['Email'])
    
    inputFirstName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]')
    inputFirstName.send_keys(line['First Name'])
    
    inputLastName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]')
    inputLastName.send_keys(line['Last Name '])
    
    inputRole = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]')
    inputRole.send_keys(line['Role in Company'])
    
    inputAddress = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]')
    inputAddress.send_keys(line['Address'])
    
    inputPhone = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]')
    inputPhone.send_keys(line['Phone Number'])
    
    buttonSubmit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    buttonSubmit.click()
    
time.sleep(20)

driver.quit()
