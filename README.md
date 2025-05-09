# 🤖 RPA Challenge Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

Bot desenvolvido em Python para automação de processos e resolução de desafios complexos de RPA (Robotic Process Automation). 
Desenvolvido para demonstrar técnicas avançadas de automação em cenários reais.

## 🎯 Objetivo do Projeto
Resolver desafios de RPA que envolvem:
- Interação com sistemas legados
- Processamento de dados estruturados e não estruturados
- Automação cross-platform (web/desktop)
- Manipulação de diferentes formatos de arquivos
- Integração entre múltiplas tecnologias

## ✨ Funcionalidades 
- **Automação web inteligente** com Selenium (incluindo wait conditions e dynamic XPath)
- **ETL de dados** com manipulação de Excel/CSV via Pandas
- **OCR básico** para reconhecimento de elementos em telas usando OpenCV
- **Pipeline completo** desde coleta até geração de relatórios
- **Gestão de configurações** através de variáveis de ambiente (.env)
- **Modo headless** para execução em servidores sem interface gráfica

## 🧩 Desafios Superados
1. **Dynamic Element Handling**  
   Solução: Implementação de wait conditions personalizadas e XPath adaptativos

2. **Cross-Platform File Management**  
   Solução: Sistema unificado para tratamento de paths diferentes (Windows/Linux)

3. **Error Recovery**  
   Solução: Mecanismo de retry automático para operações instáveis

4. **Data Validation**  
   Solução: Checksums e verificações de integridade de arquivos
   
## 📦 Pré-requisitos

- Python 3.8+
- Google Chrome instalado
- Git (para clonar o repositório)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/jvabreucunha/rpa_test.git
cd rpa_test
```
2. Instale as dependências:

```bash
pip install -r requirements.txt
```
3.Configure o WebDriver:
-Baixe o ChromeDriver compatível com sua versão do Chrome
-Coloque o executável na pasta drivers/

## 🧩 Tecnologias Utilizadas

- **Selenium** - Automação web  
- **PyAutoGUI** - Automação de interface  
- **Pandas** - Manipulação de dados  
- **OpenCV** - Processamento de imagens  
- **Python-dotenv** - Gerenciamento de variáveis de ambiente
