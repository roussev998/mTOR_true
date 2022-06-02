#!/usr/bin/env python3

import pandas as pd

df1 = pd.read_csv(input(""))
df2 = pd.read_csv(input(""))

df1.iloc[:,1] = df2.iloc[:,1]

df1.to_csv(input(""), header = True, index = False)



