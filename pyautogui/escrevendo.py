#Crie um programa que peça ao usuário, login e senha, e copie e cole dentro de um bloco de notas

import pyautogui
import pyperclip

pyautogui.alert(text='Inicio da execução')

usuario = pyautogui.prompt(text='Informe o seu nome Pietra: ',title='login')
senha = pyautogui.password(text='Digite a senha Pietra: ',title='login 123456', mask='*')

def escrever(texto):
	pyperclip.copy(texto)
	pyautogui.hotkey('ctrl','v')

pyautogui.click(1523,404,duration = 2)

escrever(f'Usuário informado: {usuario}')
pyautogui.press('enter')
escrever(f'Senha informada: {senha}')