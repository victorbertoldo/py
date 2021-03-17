from selenium.webdriver import Chrome
import time as t


browser = Chrome()
browser.get('https://www.goiania.go.gov.br/')
browser.maximize_window()

t.sleep(3)

'''
Se houver necessidade de confirmar o acesso ao site por conta 
de certificado invalido, basta desconmentar os passos abaixo:

----------------------------------------------------------
    avancar = browser.find_element_by_id('details-button')
    avancar.click()

    t.sleep(1)

    ir_para = browser.find_element_by_id('proceed-link')
    ir_para.click()
----------------------------------------------------------    
'''
contribuinte = browser.find_element_by_xpath('/html/body/main/section[4]/div[1]/div[6]/div[4]/a')
contribuinte.click()


# browser.quit()