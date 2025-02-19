import pandas as pd

csv_directory = '.'

# csv_files = [
#     'gossipcop_fake_final.csv',
#     'gossipcop_real_final.csv',
#     'politifact_fake_final.csv',
#     'politifact_real_final.csv'
# ]

# csv_files = [
#     'ISOT_fake.csv',
#     'ISOT_real.csv'
# ]

csv_files = [
    'ISOT_combined.csv',
    'FakeNewsNet_combined.csv'
]

dfs = []

for file in csv_files:
    try:
        df = pd.read_csv(file)
        if file == 'FakeNewsNet_combined.csv':
            df['date'] = df['date'].astype(str).str[:10]
        # print(f"Len of {file}: {len(df)} rows.")
        dfs.append(df)
        # print(dfs)
    except Exception as e:
        print(f"Error reading {file}: {e}")

if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    output_csv = 'Fake_News_KO.csv'
    # output_csv = 'ISOT_combined.csv'
    combined_df.to_csv(output_csv, index=False)
    print(f"Len of combined: {len(combined_df)} rows.")

#10988 rows for FakeNewsNet
#44888 rows for ISOT