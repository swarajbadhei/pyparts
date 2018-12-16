import pandas as pd
import numpy as np
df=pd.read_csv('C:\\Users\\Swaraj Badhei\\Desktop\\calc.csv')
print(df)
print('cgpa more than 9')
print(df.loc[df['cgpa']>9])
print('cgpa less than 5')
print(df.loc[df['cgpa']<5])
print('students failed in english')
print(df.loc[df['eng']<20])