import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# this version has errors with labels and legend colors
# import mplcursors

df = pd.read_csv('data/trackmate_JHH4_A2.csv', index_col=False)
print(df)

tracker = np.array(df['tracker'])
tracks = np.array(df.tracks)
seconds = np.array(df['seconds'])
print(tracker, tracks, seconds)

fig, ax = plt.subplots()

scatter = ax.scatter(seconds, tracks)
plt.legend([tracker[0], tracker[1], tracker[2], tracker[3], tracker[4], tracker[5]])

# produce a legend with tracker types
# legend1 = ax.legend(*scatter.legend_elements(), labels=tracker,
#                     loc="upper right", title="Trackers")
# ax.add_artist(legend1)
ax.grid(True)

plt.show()

# this block worked but the labels overlapped and I couldn't find a good way so they wouldn't overlap
# for i in range(len(tracker)):
#     label = tracker[i]
#
#     plt.annotate(label,  # this is the text
#                  (seconds[i], tracks[i]),  # these are the coordinates to position the label
#                  textcoords="offset points",  # how to position the text
#                  xytext=(10, 10),  # distance from text to points (x,y)
#                  ha='center')  # horizontal alignment can be left, right or center


# block for generating 0, 1 based colors
# for i in range(len(tracker)):
#     # value = (np.random.randint(0, 100)) / 100
#     # color = (value, value**2, math.sqrt(value), value)  # create RGB color based on tracker
#     # print(color)
#     plt.scatter(seconds[i], tracks[i], c=colors[i], label=tracker[i])
