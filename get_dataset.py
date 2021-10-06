import os

import pandas as pd

import utils


i = 0
list_dir = os.listdir('./output')

dfs = []
for f in list_dir:
    if len(dfs) > 0: dfs = [dfs]

    i = i + 1

    df = pd.read_csv('./output/' + f, low_memory=False)

    print(str( i / len(list_dir)) + "")

    dfs.append(df)

    dfs = pd.concat(dfs)


dfs.to_csv("final_dataset.csv", index=False)
