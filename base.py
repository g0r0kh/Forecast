import pandas as pd
import numpy as np

# import xlsx
data = pd.read_excel('source/task_sample.xlsx',
                     sheet_name='Лист1')
# transform dtype
data[['time_index']] = data[['time_index']].astype(str)
# add columns
data['year'] = data['time_index'].str[:4].astype(str)
# find perc
