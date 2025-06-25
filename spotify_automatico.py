import pyautogui as pag
from time import sleep

#pag.displayMousePosition()

pag.press('win')
sleep(2)
pag.write('chrome')
pag.press('enter')
pag.moveTo(289,66)
sleep(2)
pag.click()
sleep(2)
pag.write('https://open.spotify.com/intl-pt/')
pag.press('enter')
sleep(2)
pag.moveTo(907,118)
pag.click()
pag.write('ME JALO')
pag.press('enter')
pag.moveTo(896,325,duration=1)
pag.click()
pag.click()