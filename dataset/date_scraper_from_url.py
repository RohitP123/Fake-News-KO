import pandas as pd
from newspaper import Article
import time

def get_publish_date(url):
    """
    Get publish date of articles
    """
    try:
        if not isinstance(url, str) or pd.isna(url):
            print("Invalid URL")
            return None
        
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        article = Article(url)
        article.download()
        article.parse()
        return article.publish_date 
    except Exception as e:
        # print(f"Error processing {url}: {e}")
        return None

csv_file = 'politifact_real.csv'
df = pd.read_csv(csv_file)

# print(df.columns)

publish_dates = []


for idx, row in df.iterrows():
    if (idx+1) % 100 == 0:
        print(f"Processing {idx+1}/{len(df)}")
    url = row['news_url']
    # print(f"Processing {url} ({idx+1}/{len(df)})")
    pub_date = get_publish_date(url)
    publish_dates.append(pub_date)
    # print(f"Publish date: {pub_date}")
    # print()
    # time.sleep(1)  

# for idx, row in df_subset.iterrows():
#     url = row['news_url']
#     print(f"Processing {url} ({idx+1}/{len(df_subset)})")
#     pub_date = get_publish_date(url)
#     publish_dates.append(pub_date)
#     time.sleep(1)


df['date'] = publish_dates

df_valid = df.dropna(subset=['date'])

df_valid['label'] = 1

df_final = df_valid[['label', 'title', 'date']]

print("Num Valid:", len(df_final))
print("Total:", len(df))
#gossipcop_fake: 2772/5323 valid
#gossipcop_real: 8033/16817 valid
#politifact_fake: 153/452 valid
#politifact_real:  30/624 valid

# output_csv = 'gossipcop_fake_final.csv'

df_final.to_csv("politifact_real_final.csv", index=False)

