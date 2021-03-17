import pyautogui as ui

# Capturar as coordenadas da tela
# ui.sleep(5)
# print(ui.position())

ui.click(x=3050, y=1325, duration=1)


ui.hotkey('ctrl','f')
ui.sleep(3)
ui.typewrite('Marina')
ui.sleep(15)
ui.press('enter')

ui.sleep(1)

qtde = 0

ui.typewrite('Oi, tudo bem?!')
ui.press('enter')
ui.sleep(5)
ui.typewrite('Como vai?!')
ui.press('enter')
ui.sleep(5)

while qtde < 100000:
    qtde += 1
    ui.typewrite('E agora?!')
    ui.press('enter')
    ui.sleep(5)
