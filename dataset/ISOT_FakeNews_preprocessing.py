import pandas as pd
from datetime import datetime

def parse_date(date_str):
    for fmt in ("%B %d, %Y", "%d-%b-%y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except Exception:
        return pd.NaT

input_csv = 'ISOT/Fake.csv'

df = pd.read_csv(input_csv)

df['label'] = 0

df['date'] = df['date'].apply(parse_date)

df = df.dropna(subset=['date'])

df['date'] = df['date'].dt.strftime('%Y-%m-%d')

columns_to_keep = ['title', 'date']

df_final = df[['label'] + columns_to_keep]

df_final.to_csv('ISOT_fake.csv', index=False)
