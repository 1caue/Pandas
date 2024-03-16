import openpyxl

book = openpyxl.Workbook

print(book.sheetnames)

book.create_sheet("Frutas")

fruits_page = book['Frutas']
fruits_page.append(['Banana', '5', 'R$2,50'])
fruits_page.append(['Maça', '17', 'R$8,70'])
fruits_page.append(['Pera', '10', 'R$3,25'])
fruits_page.append(['Uva','4','R$10,90'])

book.save('Frutas.xlsx')