import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


# Colors
colors = ['#958EA2', '#582156', '#385E88', '#AA2070', '#EC008C']

# Constructing the DataFrame directly from the provided data  
data = [
    # {'sparsity': 0.0, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.1, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.2, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.3, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.4, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.5, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.6, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.7, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.8, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
    # {'sparsity': 0.9, 'dense': 0.0, 'dss': 0.0, 'dsd': 0.0},
]

# Extracting layer labels and corresponding times for each layout
sparsity_ratios = [d['sparsity'] for d in data]
dense_time = [d['dense'] for d in data]
dss_time = [d['dss'] for d in data]
dsd_time = [d['dsd'] * 2 for d in data]

# Number of groups  
num_ratios = len(sparsity_ratios)
  
# Setting up the bar width  
bar_width = 0.15 
  
# Setting the position of the bars on the x-axis  
r1 = np.arange(num_ratios)
r2 = [x + bar_width for x in r1]  
r3 = [x + bar_width for x in r1]  
r4 = [x + bar_width for x in r1]  
r5 = [x + bar_width for x in r1]

# Creating the figure
plt.figure(figsize=(4, 3))
  
# Creating the bar plot
line_colors = ['#0C408C', '#8186D8', '#BF84BA', '#FFDFD3', '#171A39']
plt.plot(r1, dense_time, color=line_colors[0], marker='o', label='Dense', markersize=3, linewidth=1)
plt.plot(r2, dss_time, color=line_colors[1], marker='^', label='DSS', markersize=3, linewidth=1)
plt.plot(r3, dsd_time, color=line_colors[2], marker='s', label='DSD', markersize=3, linewidth=1)
  
# Adding labels  
plt.xlabel('Sparsity Ratio', fontweight='bold')  
plt.ylabel('Execution Time', fontweight='bold')
plt.xticks([r + bar_width for r in range(num_ratios)], sparsity_ratios)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))  
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0)) 

# Creating legend & title for the bar plot  
plt.legend(bbox_to_anchor=(0.2, 1.02, 1.0, 1.02), loc='lower left', ncol=3, mode="expand", borderaxespad=0., frameon=False, fontsize=8)

# Saving the figure (optional)  
plt.tight_layout()
plt.savefig('./experiments/ablation-operator/exp-ablation-operator-mlp.pdf')
