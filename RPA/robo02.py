import pyautogui as ui

# usando as teclas do teclado para abrir um programa
ui.hotkey('win','r')
ui.sleep(1)
ui.typewrite('notepad')
ui.press('enter')

# escrevendo texto
ui.sleep(1)
ui.typewrite('Olá!!! Sou um bot.')
ui.sleep(2)

# capturando a janela aberta
janela = ui.getActiveWindow()
# fechando janela
janela.close()
# na box de confirmação para salvar o arquivo, selecionar a opção da direita
ui.press('right')
ui.sleep(2)
ui.press('enter')
