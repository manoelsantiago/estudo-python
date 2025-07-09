import pyautogui

pyautogui.alert(text='Início da execução!',title='Automação de login',button='OK')

# prompt que captura o email
# email = pyautogui.prompt(text = 'Informe seu e-mail',title='Email obrigatório')
# print(f'Email innformado: {email}')

resposta = pyautogui.confirm(text = 'Deseja continuar?',title = 'Confirmação', buttons = ['sim','não','cancelar'])

if resposta == 'sim':
	print(f'If do SIM - Você respondeu: {resposta}')
elif resposta == 'não':
	print(f'If do NÃO - Você respondeu: {resposta}')
elif resposta == 'cancelar':
	print(f'If do CANCELAR - Você respondeu: {resposta}')
	

pyautogui.alert(text = 'Fim da execução!', title='Aviso',button='Sair')