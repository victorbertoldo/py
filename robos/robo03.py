from openpyxl import Workbook

print("Iniciando nosso robô...")
print("Lendo dados do arquivo de texto.")
file_txt = open('gastos.txt', 'r', encoding='utf-8')

arq = file_txt.read()
print(arq)

lista_txt = arq.splitlines()
print(lista_txt)

for i in range(0, len(lista_txt)):
    lista_txt[i] = lista_txt[i].split(',') # separando a lista por linhas

print(lista_txt)

# Criando arquivo excel

wb = Workbook()
ws = wb.active

for row in lista_txt:
    ws.append(row)

wb.save('gastos.xlsx')    