import pandas as pd
DF1=pd.read_excel('../../4.프로젝트(6조)/07_24_05_P.xlsx')
DF1.to_csv('encoding.csv',encoding='utf-8')