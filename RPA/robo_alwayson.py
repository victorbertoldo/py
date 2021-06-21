import pyautogui as ui

# Capturar as coordenadas da tela
ui.sleep(5)
print(ui.position())

ui.moveTo(x=3381, y=753, duration=1)
ui.click(x=3476, y=646)

for i in range(0,900):
    print(i)
    # Movendo o mouse para as coordenadas
    # ui.moveTo(x=3381, y=753, duration=1)
    # ui.click(x=3476, y=646)

    # Clicando na coordenadas 1x
    # ui.click(x=3381, y=753)

    ui.sleep(1)

    ui.scroll(-10)
    # ui.click(x=2875, y=31)
    ui.press('down')

    ui.scroll(20)


    # ui.click(x=3358, y=14)

    # ui.sleep(30)

for i in range(0,1200):
    print(i)
    # Movendo o mouse para as coordenadas
    # ui.moveTo(x=3381, y=753, duration=1)
    # ui.click(x=3476, y=646)

    # Clicando na coordenadas 1x
    # ui.click(x=3381, y=753)

    ui.sleep(1)

    ui.scroll(-10)
    # ui.click(x=2875, y=31)
    ui.press('up')

    ui.scroll(20)    