import pyautogui as ui

# Capturar as coordenadas da tela
# ui.sleep(5)
# print(ui.position())

for i in range(0,30):
    print(i)
    # Movendo o mouse para as coordenadas
    ui.moveTo(x=3381, y=753, duration=1)

    # Clicando na coordenadas 1x
    ui.click(x=3381, y=753)

    ui.sleep(2)

    ui.click(x=2875, y=31)

    ui.sleep(1)

    ui.click(x=3358, y=14)

    ui.sleep(30)