import pandas as pd
import numpy as np
# import itertools

# xlsx source import
data = pd.read_excel('source/task_sample.xlsx',
                     sheet_name='Лист1')
# transform dtype
data[['time_index']] = data[['time_index']].astype(str)
# add columns
data['iter_str'] = data['time_index'].str[:4].astype(str) + data['task_mark'].astype(str)
# rename columns
data = data.rename(columns={'values':'vals'})
sort_list = sorted(set(data['iter_str']))

# list catch outliers
occup = []

for i in sort_list:
    a = data[data['iter_str'] == i]
    a = a.reset_index()
    # symmetric distribution
    out_bottom = (np.percentile(np.array([a.vals]), 25) -
                  (np.percentile(np.array([a.vals]), 75) - np.percentile(np.array([a.vals]), 25)) * 1.5).astype(int)
    # .astype(str))
    # negatively skewed
    if out_bottom <= np.min(np.array([a.vals])):
        # try Median - (Q3-Q2)*1.5
        out_bottom_n = (np.percentile(np.array([a.vals]), 25) -
                        (np.percentile(np.array([a.vals]), 75) - np.median(np.array([a.vals]))) * 1.5).astype(float)
        occup.append(out_bottom_n)
    else:
        occup.append(out_bottom)
# convert statistic iter list 2 Dataframe
data_distr = pd.DataFrame([list(x) for x in zip(sort_list, occup)])
# merge main data with statistics
data.merge(data_distr, left_on='iter_str', right_on=0)


