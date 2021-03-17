import pyautogui as ui

def robo_notepad():
    """ 
        Utilizando as teclas do teclado para abrir um programa: Notepad

        * Abre o notepad
        * Escreve uma msg
        * Fecha o programa

        É necessário inserir o argumento FAILSAFE da lib pyautogui

    """

    ui.FAILSAFE = False

    ui.sleep(1)
    ui.hotkey('win','r')
    ui.sleep(1)
    ui.typewrite('notepad')
    ui.sleep(1)
    ui.press('enter')

    
    ui.sleep(1)
    ui.typewrite('Olá!!! Sou um bot.')
    ui.sleep(2)

    
    janela = ui.getActiveWindow()
    

    janela.close()
    

    ui.press('right')
    ui.sleep(2)
    ui.press('enter')

robo_notepad()