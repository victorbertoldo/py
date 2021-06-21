from openpyxl import load_workbook

wb = load_workbook(filename='nomes.xlsx')

Planilha = wb['Planilha1']

for i in range(2,5):
    print("%s tem %s anos." % (Planilha['A%s' % i].value, Planilha['B%s' % i].value))