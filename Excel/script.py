import pandas as pd   # Max Linhas: 7
from IPython.display import display

valores_df = pd.read_excel(r'C:\Users\CAUÊ\Documents\Pandas\Excel\tst.xlsx')

valores_dez = pd.read_excel(r'C:\Users\CAUÊ\Documents\Pandas\Excel\valores-dez.xlsx')

valores_dez['Colunas1'] = valores_dez['Colunas2'].apply(lambda x: x * 3)

valores_dez.to_excel('Nova_Tabela.xlsx', index=False)
display(valores_dez)
