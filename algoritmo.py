import pyautogui
import time

pyautogui.FAILSAFE = False


print(pyautogui.position())
# Dá tempo para você posicionar o mouse e observar o movimento
time.sleep(2)
# Move o mouse para a posição (100, 100) durante 1 segundo
pyautogui.moveTo(100, 100, duration=1)

