from IPython.display import display
import pandas as pd

planilha = pd.read_excel(r'c:\Users\CAUÊ\Documents\Pandas\Script\tst.xlsx')
planilha.loc[planilha["Cor"] == "Azul", "Quantidade"] = 1 # Modificando Células na tabela

display(planilha)

