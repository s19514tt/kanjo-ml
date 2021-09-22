import pandas as pd

""" df = pd.read_csv('./final.csv')
df = df.dropna(how='all', axis=1)
df.to_csv('./tmp1.csv') """

df = pd.read_csv('./tmp1.csv')
df.dropna().to_csv('./learndata.csv')
