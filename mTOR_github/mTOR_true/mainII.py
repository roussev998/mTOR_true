"""to create the heat map as a csv file with on and off neext to each other"""

import pandas as pd
from tkinter import filedialog as fd

df1 = fd.askopenfilename(title='Open the Ist csv from the order of the names')
df2 = fd.askopenfilename(title='Open the IIst csv from the order of the names')
df3 = fd.askopenfilename(title='Open the IIIst csv from the order of the names')
df4 = fd.askopenfilename(title='Open the IVst csv from the order of the names')

df1 = pd.read_csv(df1)
df2 = pd.read_csv(df2)
df3 = pd.read_csv(df3)
df4 = pd.read_csv(df4)

df1 = df1.reindex(index=df2.index)
df3 = df3.reindex(index=df2.index)
df4 = df4.reindex(index=df2.index)

ready_df = pd.concat([df1,df2,df3,df4], axis =1)

col_names = ['t = ' + str(i) for i in range(0, len(list(ready_df)))]
ready_df.columns = col_names

ready_df.to_csv("heatmap.csv")