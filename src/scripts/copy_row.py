from openpyxl import Workbook, load_workbook, utils



# Abre o arquivo Excel
wb = load_workbook("teste.xlsx")

# Seleciona a primeira planilha
sheet = wb.active

# Obtém a linha 5
row = sheet[5]

# Copia a linha para uma nova variável
copied_row = row[:]

# Insere a linha copiada na linha 10
sheet.insert_rows(10, copied_row)

# Salva as alterações no arquivo
wb.save("teste_1.xlsx")