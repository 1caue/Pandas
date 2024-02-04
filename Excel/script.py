import pandas as pd   # Max Linhas: 7
from IPython.display import display

valores_df = pd.read_excel(r'C:\Users\CAUÊ\Documents\Pandas\Excel\tst.xlsx')
#valores_df.loc[:, 'Zero'] = 300 / 3
valores_df = valores_df.drop('Quantidade', axis=1)
display(valores_df)
 


