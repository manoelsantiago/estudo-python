import pyautogui
import pyperclip

def escreverFrase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(1450,239,duration=2)

escreverFrase('Automação é incrível!')