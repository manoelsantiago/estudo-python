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

nome = 'Manoel Santiago'

# abrir site
webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
sleep(3)
pyautogui.moveTo(934,373,duration=0.5)
pyautogui.scroll(-770)

# localizar o campo nome e escrever nome e clicar em alerta
centro = pyautogui.locateCenterOnScreen('seunome.png')
pyautogui.click(centro[0],centro[1],duration=1)
pyautogui.typewrite(nome)
centro = pyautogui.locateCenterOnScreen('botaoAlerta.png')
sleep(1)
pyautogui.click(centro[0],centro[1], duration=1)
sleep(1)
# fechar o alerta
centro = pyautogui.locateCenterOnScreen('botaoOK.png')
pyautogui.click(centro[0],centro[1],duration=1)
# rolar pagina para cima depois para sessao downloads
pyautogui.scroll(1000)
sleep(1)
pyautogui.scroll(-2000)
sleep(1)
centro = pyautogui.locateCenterOnScreen('excel.png')
pyautogui.click(centro[0],centro[1]+50,duration=1)
sleep(1.5)
centro = pyautogui.locateCenterOnScreen('salvar.png')
pyautogui.click(centro[0],centro[1],duration=0.5)
sleep(2)
centro = pyautogui.locateCenterOnScreen('arquivoPDF.png')
pyautogui.click(centro[0],centro[1]+50,duration=0.5)
sleep(1.5)
centro = pyautogui.locateCenterOnScreen('salvar.png')
pyautogui.click(centro[0],centro[1],duration=0.5)
sleep(1)
pyautogui.alert('..:: VOCÊ TERMINOU ::..')

