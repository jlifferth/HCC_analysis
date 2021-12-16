import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# this version correctly assigns labels and legend colors

df = pd.read_csv('data/trackmate_JHH4_A2_LoG.csv', index_col=False)
print(df)

tracker = np.array(df['tracker'])
tracks = np.array(df.tracks)
seconds = np.array(df['seconds'])
colors = ['b', 'g', 'r', 'c', 'y', 'k']
print(tracker, tracks, seconds)

for i in range(len(tracker)):
    plt.scatter(seconds[i], tracks[i], c=colors[i], label=tracker[i],
                s=175, alpha=0.5)

plt.title('Performance of tracking algorithms for JHH4_A2 cell line')
plt.xlabel('Algorithm run time')
plt.ylabel('Tracks found')
plt.legend()
plt.grid(True)
plt.show()
