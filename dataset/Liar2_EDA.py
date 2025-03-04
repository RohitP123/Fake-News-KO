import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Liar2_combined.csv")

df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df['year'] = df['date'].dt.year
total_records = len(df)

year_counts = df['year'].value_counts().sort_index()
year_percentages = (year_counts / total_records) * 100

print("\nPercentage of Data per Year:")
print(year_percentages)

year_percentages.plot(kind='bar', title='Data Percentage per Year', ylabel='Percentage (%)')
plt.xlabel("Year")
plt.show()

label_counts = df['label'].value_counts()
print("\nLabel Counts: ")
print(label_counts)


split_date = df['date'].quantile(0.8)
split_date = split_date.strftime("%Y-%m-%d")
print("\nSplit Date:")
print(split_date)