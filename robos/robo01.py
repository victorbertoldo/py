from openpyxl import Workbook

wb = Workbook()

nome_arq = "teste01.xlsx"

ws1 = wb.active
ws1.title = "Planilha Teste 01"

dados = [
    ['Ano', 'Lucro', 'Custos'],
    [2015, '30%', '40%'],
    [2016, '34%', '50%'],
    [2017, '20%', '60%']
]

for l in dados:
    ws1.append(l)

ws2 = wb.create_sheet(title='Planilha teste 02')
ws2['D3'] = 'Doidera'

wb.save(filename=nome_arq)    