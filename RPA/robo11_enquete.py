from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

browser = Chrome()
browser.get('https://ferendum.com/pt/')
browser.maximize_window()
t.sleep(3)

titulo = browser.find_element_by_name('titulo')
titulo.send_keys('A automação é uma coisa boa? (victor Bertoldo)')

descricao = browser.find_element_by_name('descripcion')
descricao.send_keys('Os robos estão cada dia mais inseridos na nossa realidade.')

nome = browser.find_element_by_name('creador')
nome.send_keys('Jão das Covis')

mail = browser.find_element_by_css_selector('input[type="email"]')
mail.send_keys('jaocovis@bol.com.br')

op1 = browser.find_element_by_id('op1')
op1.send_keys('Não sei opinar. Ass.: Glória Pires.')

op2 = browser.find_element_by_id('op2')
op2.send_keys('Sim, me deixam mais produtivo.')

op3 = browser.find_element_by_id('op3')
op3.send_keys('Sim, tenho preguiça de fazer coisas repetitivas.')

op4 = browser.find_element_by_id('op4')
op4.send_keys('Não, tenho medo de perder o emprego.')

op5 = browser.find_element_by_id('op5')
op5.send_keys('Não, prefiro pessoas à robos.')

config_anonima = browser.find_element_by_name('config_anonimo')
config_anonima.click()
config_anonima = browser.find_element_by_name('config_anonimo')
config_anonima.click()
config_anonima = browser.find_element_by_name('config_anonimo')
config_anonima.click()
config_anonima = browser.find_element_by_name('config_anonimo')
config_anonima.click()
config_anonima = browser.find_element_by_name('config_anonimo')
config_anonima.click()

