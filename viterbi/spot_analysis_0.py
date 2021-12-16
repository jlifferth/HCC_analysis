# this script is to analyze spots and animate them in pyplot
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np

df = pd.read_csv('Spots in tracks statistics.csv', usecols=['ID', 'POSITION_X', 'POSITION_Y', 'FRAME'])
print(df.columns)
df_0 = df[df['FRAME'] == 0]

plt.scatter(x=df_0['POSITION_X'], y=df_0['POSITION_Y'])
plt.show()
