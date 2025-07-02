import pyautogui
from time import sleep

# https://www.crazygames.com/game/doge-miner-2?_gl=1*f430bs*_ga*NDExNTQ3OTQ4LjE3NTEyODAyMTA.*_ga_37GXT4VGQK*czE3NTE0NTA2NzAkbzYkZzEkdDE3NTE0NTA3NzMkajM0JGwwJGgw
# criar uma automação que clique e passe uma fase do jogo acima

pyautogui.moveTo(1226,716,duration=2.5)
for i in range(200):
    sleep(0.1)
    pyautogui.click()