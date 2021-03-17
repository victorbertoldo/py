import rpa as r
import pyautogui as ui

r.init()
r.url('http://www.google.com')
r.url()
janela = ui.getActiveWindow()
janela.maximize()
r.wait(2.0)
# também é possivel realizar uma busca no css, os objetos que podem ser utilizados na busca estão listados no arquivo 'css-busca.txt'
r.type('//*[@name="q"]', 'RPA[enter]')
r.wait(0.5)
r.snap('page', 'rpa_page01.png')
r.wait(2.0)
r.close()