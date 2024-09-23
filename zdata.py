import pandas as pd
import numpy as np

file_path = 'zdata.xlsx'
df = pd.read_excel(file_path)
z = df.to_numpy()
print(z)