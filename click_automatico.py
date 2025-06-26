import pyautogui as pag
from time import sleep
import keyboard

# pag.displayMousePosition()

pag.press('win')
pag.write('chrome')
pag.press('enter')
sleep(2)
pag.moveTo(964,581)
sleep(2)
pag.click()
pag.write('https://www.crazygames.com/game/capybara-clicker-2')
sleep(2)
pag.press('enter')
sleep(2)
pag.moveTo(913,606)
sleep(2)
pag.click()
sleep(5)


keyboard.wait('s')
for i in range(1000000000000000):
    pag.doubleClick()
    if keyboard.is_pressed('q'):
        break