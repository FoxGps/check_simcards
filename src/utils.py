import pandas as pd
from dotenv import load_dotenv
import requests, os

load_dotenv()

def tem_19_digitos(numero):
    if numero != None:
      return bool(len(numero) >= 18)
    return False

def ler_planilha(caminho_arquivo):
  return pd.read_excel(caminho_arquivo, engine='openpyxl')
  
def api_connect():
  URL_TRACCAR = os.getenv("URL_TRACCAR")
  TOKEN = os.getenv("TOKEN_TRACCAR")
  
  url = f"{URL_TRACCAR}/api/devices"
  headers = {
    "Authorization": f"Bearer {TOKEN}"
  }

  response = requests.get(url, headers=headers)

  if response.status_code ==  200:
    veiculos = response.json()
  else:
    print(f"Erro ao acessar a API: {response.status_code}")
    veiculos = []

  df = pd.DataFrame(veiculos)
  df.to_excel('data/devices_all.xlsx', index=False)
  print("Dados dos veículos exportados para veiculos.xlsx")
  return veiculos
