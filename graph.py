
import numpy as np
from base import data
import matplotlib.pyplot as plt



data = data.astype({'time_index': 'datetime64[ns]'})
# tmp flt
data = data[data['task_mark'] == 'task_1']
# rnm columns
data = data.rename(columns={1:'lim_outl'})

# decimals = num - int(num)

data['color'] = np.where(data.lim_outl - data.lim_outl.astype(int) != 0, 'r', 'k')

fig, ax = plt.subplots(figsize=(12, 6), layout='constrained')

#data draw
ax.plot(data['time_index'].values, data['vals'].values, linewidth=0.5)
#outlier draw
ax.scatter(data['time_index'].values, data['out_task'].values, marker='o', color='r')
#outlier limits line draw
ax.plot(data['time_index'].values, data['lim_outl'].values, color='k', dashes=[0, 1, 1], linewidth=0.5)
#outlier limits scatter draw color=data['color'].values
ax.scatter(data['time_index'].values, data['lim_outl'].values, marker='2', color=data['color'].values, s=0.69)



plt.xticks(rotation=90)
#
#
#
plt.grid()
plt.show()