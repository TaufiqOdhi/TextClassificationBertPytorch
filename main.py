import pandas as pd

datapath = 'bbc-text.csv'
df = pd.read_csv(datapath)
df.head()