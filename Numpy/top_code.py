import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arq = r'C:\Users\CAUÊ\Documents\Pandas\Numpy\gastos.xlsx'

rd1 = pd.read_excel(arq, sheet_name='Plan1')
rd2 = pd.read_excel(arq, sheet_name='Plan2')
rd3 = pd.read_excel(arq, sheet_name='Plan3')

rd_all = pd.concat([rd1, rd2, rd3])
print(rd_all['Mês'])

