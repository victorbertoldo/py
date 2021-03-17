import rpa as r
import pyautogui as ui

r.init()
r.url('http://www.google.com')
r.url()
janela = ui.getActiveWindow()
janela.maximize()
r.wait(2.0)
r.type('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input', 'RPA[enter]')
r.wait(0.5)
r.snap('page', 'rpa_page.png')
r.wait(2.0)
r.close()