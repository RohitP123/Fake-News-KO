import pandas as pd
import os

folder = "Liar2"
filenames = ["train.csv", "test.csv", "valid.csv"]

dfs = []

for file in filenames:
    filepath = os.path.join(folder, file)
    df = pd.read_csv(filepath)

    df = df[['label', 'statement', 'date']]
    
    df['label'] = df['label'].apply(lambda x: 0 if x in [0, 1, 2] else 1)
    
    df.rename(columns={'statement': 'title'}, inplace=True)
    df['date'] = pd.to_datetime(df['date']).dt.strftime("%Y-%m-%d")
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

combined_df.to_csv("Liar2_combined.csv", index=False)
