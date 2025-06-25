import pyautogui as pag
from time import sleep

# pag.displayMousePosition()

pag.press('win')
pag.write('chrome')
pag.press('enter')
pag.moveTo(960,581)
sleep(2)
pag.click()
sleep(2)
pag.write('https://www.youtube.com/')
pag.press('enter')
sleep(2)
pag.moveTo(820,121)
pag.click()
pag.write('Drake - God Plan')
pag.press('enter')
pag.moveTo(660,394,duration=1)
pag.click()