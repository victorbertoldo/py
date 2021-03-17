import pyautogui as ui

ui.hotkey('win', 'r')
ui.sleep(1)
ui.write(r'"C:\Users\victor.bertoldo\Downloads\RPA.pbix"')
ui.sleep(1)
ui.press('enter')
ui.sleep(18)

ui.click(x=4884, y=116)
ui.sleep(8)
ui.click(x=5568, y=22)
ui.sleep(1)
ui.press('left')
ui.press('enter')