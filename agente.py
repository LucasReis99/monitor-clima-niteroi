import requests
import pandas as pd
from datetime import datetime
import os

def buscar_e_salvar():
    # API da Open-Meteo (Niterói)
    url = "https://api.open-meteo.com/v1/forecast?latitude=-22.88&longitude=-43.12&current_weather=true"
    
    response = requests.get(url)
    dados = response.json()
    temp = dados['current_weather']['temperature']
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Criar um DataFrame com os novos dados
    novo_dado = pd.DataFrame([[horario, temp]], columns=['Data/Hora', 'Temperatura'])

    # Salvar ou anexar ao arquivo CSV
    arquivo = 'historico_temperatura.csv'
    if not os.path.isfile(arquivo):
        novo_dado.to_csv(arquivo, index=False)
    else:
        novo_dado.to_csv(arquivo, mode='a', header=False, index=False)
    
    print(f"Dados salvos: {horario} - {temp}°C")

if __name__ == "__main__":
    buscar_e_salvar()
