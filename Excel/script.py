import pandas as pd   # Max Linhas: 7
from IPython.display import display

valores_df = pd.read_excel(r'C:\Users\CAUÊ\Documents\Pandas\Excel\tst.xlsx')

valores_dez = pd.read_excel(r'C:\Users\CAUÊ\Documents\Pandas\Excel\valores-dez.xlsx')

valores_df = valores_df.merge(valores_dez)

display(valores_df)