# DESAFIO 🥇
# 1) Navegue até o site https://cursoautomacao.netlify.app/
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
# 3) Clique em alerta, para gerar a alerta
# 4) Feche a alerta
# 5) Suba a página totalmente para cima
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"

import webbrowser
import pyautogui
from time import sleep

webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
sleep(1)
pyautogui.moveTo(934,373,duration=1)
pyautogui.scroll(-770)
centro = pyautogui.locateCenterOnScreen('seunome.png')
pyautogui.click(centro[0],centro[1],duration=2)
