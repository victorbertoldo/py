import pyautogui as ui
import rpa
import pandas as pd

rpa.init()
rpa.url('http://rpachallenge.com/')
window = ui.getActiveWindow()
window.maximize()

ui.sleep(5)

rpa.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'challenge.xlsx')
ui.sleep(2)

df = pd.DataFrame(pd.read_excel(r'challenge.xlsx', sheet_name='Sheet1'))

rpa.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')

for row in df.itertuples():
    rpa.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    rpa.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    rpa.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    rpa.type('//*[@ng-reflect-name="labelRole"]', row[4])
    rpa.type('//*[@ng-reflect-name="labelAddress"]', row[5])
    rpa.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    rpa.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    rpa.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
    ui.sleep(1)


ui.sleep(5)    
ui.screenshot('score.png')
rpa.close()