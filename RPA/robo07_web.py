import pyautogui as ui
import rpa as r
import pandas as pd
import os

r.init()
ui.sleep(2)
r.url('https://rpachallengeocr.azurewebsites.net/')
ui.sleep(3)
window = ui.getActiveWindow()
window.maximize()

countPage = 1
dados = pd.DataFrame()

while countPage <= 3:
    # selecionando a tabela
    r.table('//*[@id="tableSandbox"]', 'temp.csv')
    dados = dados.append(pd.read_csv('temp.csv'))
    
    # clicando no next para mostrar a proxima pagina
    r.click('//*[@id="tableSandbox_next"]')
    countPage += 1
r.close()    
os.remove('temp.csv')

print(dados)

dados.to_csv(r'webtable.csv', mode='a', index=None, header=True)