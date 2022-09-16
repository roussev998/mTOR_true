import pandas as pd
import os
from tkinter import filedialog as fd

# get the needed initial values and new attractor by choosing with gui
init = fd.askopenfilename(title='Open initial values csv')
attr = fd.askopenfilename(title='Open new attractor values csv')

# save them in python
df1 = pd.read_csv(init)
df2 = pd.read_csv(attr)

# transfer the column from df2 = attractor to df1 = initial values
df1.iloc[:,1] = df2.iloc[:,1]

# get the file name of the initial values
new_file_name = os.path.abspath(init)

# save the df1 as the new initial values put keep the same name
df1.to_csv(new_file_name, header = True, index = False) # without "" as in this way the whole proper path is saved

