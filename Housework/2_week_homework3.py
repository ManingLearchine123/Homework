import pandas as pd
excel_file = 'E:\CodesPython\Homework\side\관서별 5대범죄 발생 및 검거.xlsx'
crime = pd.read_excel(excel_file)
crime.head