import pyautogui as ui
# import op

# Capturar as coordenadas da tela
# ui.sleep(5)
# print(ui.position())

ui.doubleClick(x=45, y=285)
ui.sleep(5)
ui.write('www.udemy.com')
ui.press('enter')
ui.sleep(1)
window = ui.getActiveWindow()
window.maximize()
ui.sleep(5)

localPesq = ui.locateOnScreen(r'resources\search_udemy.png', confidence=0.9)
centerLocalPesq = ui.center(localPesq)
xPesq, yPesq = centerLocalPesq
ui.moveTo(xPesq, yPesq, duration=1)
ui.click(xPesq, yPesq)
ui.sleep(1)
ui.write('qlik sense')
ui.press('enter')
ui.sleep(3)
ui.screenshot('cursos_qlik.png')

window.close()