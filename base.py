import pandas as pd
import numpy as np

# import xlsx
data = pd.read_excel('source/task_sample.xlsx',
                     sheet_name='Лист1')
# transform dtype
data[['time_index']] = data[['time_index']].astype(str)
# add columns
data['iter_str'] = data['time_index'].str[:4].astype(str) + data['task_mark'].astype(str)
# rename columns
data = data.rename(columns={'values':'vals'})

sort_list = sorted(set(data['iter_str']))

for i in sort_list:
    a = data[data['iter_str'] == i]
    # a = a.reset_index()
# outlier prob
    data['outlier_bottom'] = ((np.percentile(np.array([a.vals]), 25) -
                              (np.percentile(np.array([a.vals]), 75)-np.percentile(np.array([a.vals]), 25))*1.5)).astype(float)
# outlier expl
# data['outlier_bottom_expl'] = ((np.percentile(np.array([data.vals]), 25) -
#                           (np.percentile(np.array([data.vals]), 75)-np.percentile(np.array([data.vals]), 25))*3)).astype(float)


# find perc

# a = np.array([data.vals])
# p = np.percentile(a, 50)
# b = np.array(arr)

# import numpy as np
# a = np.array([1,2,3,4,5])
# p = np.percentile(a, 50)

# sort_list = sorted(set(data['period']))
#
# plt.ion()
#
# for i in sort_list:
#     a = data[data['period'] == i]
#     a = a.reset_index()
#     # plt.clf()
#     plt.grid()
#
#
#     occ_list = sorted(set(a['Occupation']))
#
#     occup = []
#
#     for j in occ_list:
#         b = a[a['Occupation'] == j]
#         occup.append(b.RUR_net_000)