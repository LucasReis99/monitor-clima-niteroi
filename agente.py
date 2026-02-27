import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def buscar_e_gerar_grafico():
    # 1. Buscar os dados
    url = "https://api.open-meteo.com/v1/forecast?latitude=-22.88&longitude=-43.12&current_weather=true"
    response = requests.get(url)
    temp = response.json()['current_weather']['temperature']
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Salvar no CSV
    arquivo_csv = 'historico_temperatura.csv'
    novo_dado = pd.DataFrame([[horario, temp]], columns=['Data/Hora', 'Temperatura'])
    
    if not os.path.exists(arquivo_csv):
        novo_dado.to_csv(arquivo_csv, index=False)
    else:
        novo_dado.to_csv(arquivo_csv, mode='a', header=False, index=False)

    # 3. Gerar o Gráfico
    df = pd.read_csv(arquivo_csv)
    # Converter a coluna Data/Hora para formato de tempo real
    df['Data/Hora'] = pd.to_datetime(df['Data/Hora'])
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['Data/Hora'], df['Temperatura'], marker='o', linestyle='-', color='orange')
    plt.title('Variação da Temperatura em Niterói - RJ')
    plt.xlabel('Horário da Coleta')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvar a imagem do gráfico
    plt.savefig('grafico_temperatura.png')
    print("Gráfico atualizado com sucesso!")

if __name__ == "__main__":
    buscar_e_gerar_grafico()
