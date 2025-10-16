import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os
from datetime import datetime, timedelta
from io import StringIO

from caas_jupyter_tools import display_dataframe_to_user

np.random.seed(42)

n = 1200
start_date = datetime(2025, 1, 1)
timestamps = [start_date + timedelta(hours=int(i))
              for i in np.random.randint(0, 24*200, size=n)]

categories = ['fitness', 'tech', 'family',
              'food', 'beauty', 'finance', 'travel']
texts = [
    "Top workout for the week! #fitness #health ❤️",
    "New phone review: battery life is insane. #tech",
    "Family dinner ideas for busy parents. #family #food",
    "10 recipes under 20 minutes. #food #easymeals",
    "Skincare routine that works. #beauty",
    "Stock market basics: how to start investing. #finance",
    "Hidden travel gems for 2025. #travel",
]

rows = []
for i in range(n):
    cat = np.random.choice(
        categories, p=[0.15, 0.18, 0.14, 0.18, 0.12, 0.13, 0.10])
    base = np.random.choice(texts)
    extra_hashtags = '' if np.random.rand() > 0.6 else ' #' + ''.join(np.random.choice(
        ['fun', 'tips', 'life', 'trending', 'news'], size=np.random.randint(1, 3)))
    mentions = '' if np.random.rand() > 0.7 else ' @brand' + \
        str(np.random.randint(1, 30))
    text = f"{base}{extra_hashtags}{mentions}"
    impressions = max(50, int(np.random.lognormal(
        mean=7 if cat in ['tech', 'travel'] else 6.2, sigma=1.0)))
    likes = int(np.random.binomial(n=impressions, p=0.03 +
                (0.01 if cat in ['food', 'beauty', 'family'] else 0)))
    retweets = int(np.random.binomial(n=impressions, p=0.005 +
                   (0.005 if cat in ['tech', 'travel'] else 0)))
    replies = int(np.random.binomial(n=impressions, p=0.002))
    follower_count = max(100, int(np.random.lognormal(mean=8, sigma=1.2)))
    language = 'en' if np.random.rand() > 0.05 else 'vi'
    rows.append({
        'post_id': f'post_{i+1}',
        'timestamp': timestamps[i],
        'category': cat,
        'text': text,
        'impressions': impressions,
        'likes': likes,
        'retweets': retweets,
        'replies': replies,
        'followers_at_post': follower_count,
        'language': language
    })

df = pd.DataFrame(rows)

df.loc[np.random.choice(df.index, size=8, replace=False),
       'text'] = None
df.loc[np.random.choice(df.index, size=6, replace=False),
       'impressions'] = None


def clean_text(s):
    if pd.isna(s):
        return ""
    s = str(s)
    s = re.sub(r'http\S+', '', s)
    s = re.sub(r'@\w+', '', s)
    s = re.sub(r'#', '', s)
    s = re.sub(r'[^\x00-\x7F]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s.lower()


df['text_clean'] = df['text'].apply(clean_text)

overall_median_imp = int(df['impressions'].median(skipna=True))
df['impressions'] = df.groupby('category')['impressions'].apply(lambda x: x.fillna(
    int(x.median()) if not np.isnan(x.median()) else overall_median_imp))
df['impressions'].fillna(overall_median_imp, inplace=True)

before = len(df)
df = df[df['text_clean'].str.len() > 0].copy()
after = len(df)

df['engagement'] = df['likes'] + df['retweets'] + df['replies']
df['engagement_rate'] = df['engagement'] / df['impressions']
df['text_length'] = df['text_clean'].apply(len)
df['word_count'] = df['text_clean'].apply(lambda x: len(x.split()))
df['hashtags_count'] = df['text'].apply(
    lambda x: 0 if pd.isna(x) else x.count('#'))
df['mentions_count'] = df['text'].apply(
    lambda x: 0 if pd.isna(x) else x.count('@'))

positive_words = set(['top', 'best', 'works', 'insane',
                     'love', '❤️', 'good', 'great', 'tips', 'hidden'])
negative_words = set(['bad', 'worse', 'worst', 'hate',
                     'problem', 'issue', 'slow', 'delay', 'complaint'])


def simple_sentiment(text):
    if not text:
        return 0
    t = text.lower()
    pos = sum(1 for w in positive_words if w in t)
    neg = sum(1 for w in negative_words if w in t)
    return pos - neg


df['sentiment_score'] = df['text_clean'].apply(simple_sentiment)

df['date'] = pd.to_datetime(df['timestamp']).dt.date

agg = df.groupby('category').agg(
    posts_count=('post_id', 'count'),
    avg_impressions=('impressions', 'mean'),
    median_impressions=('impressions', 'median'),
    avg_engagement=('engagement', 'mean'),
    avg_engagement_rate=('engagement_rate', 'mean'),
    median_engagement_rate=('engagement_rate', 'median'),
    avg_word_count=('word_count', 'mean'),
    avg_sentiment=('sentiment_score', 'mean')
).reset_index().sort_values('avg_engagement_rate', ascending=False)

top_posts = df.sort_values(['category', 'engagement_rate'], ascending=[
                           True, False]).groupby('category').head(3)

os.makedirs('/mnt/data/social_media_analysis_plots', exist_ok=True)

plt.figure(figsize=(8, 5))
plt.bar(agg['category'], agg['avg_engagement_rate'])
plt.title('Average Engagement Rate by Category')
plt.xlabel('Category')
plt.ylabel('Avg Engagement Rate')
plt.tight_layout()
plt.savefig(
    '/mnt/data/social_media_analysis_plots/avg_engagement_rate_by_category.png')
plt.show()

sample = df.sample(min(400, len(df)))
plt.figure(figsize=(7, 5))
plt.scatter(sample['impressions'], sample['engagement_rate'])
plt.title('Impressions vs Engagement Rate (sample)')
plt.xlabel('Impressions')
plt.ylabel('Engagement Rate')
plt.tight_layout()
plt.savefig(
    '/mnt/data/social_media_analysis_plots/impressions_vs_engagement_rate.png')
plt.show()

daily = df.groupby(['date', 'category']).size().unstack(fill_value=0)
plt.figure(figsize=(10, 5))
daily.sum(axis=1).rolling(window=7).mean().plot()
plt.title('Overall posting volume (7-day MA)')
plt.xlabel('Date')
plt.ylabel('Posts (7-day MA)')
plt.tight_layout()
plt.savefig('/mnt/data/social_media_analysis_plots/posting_volume_7dayma.png')
plt.show()

plt.figure(figsize=(8, 5))
df.boxplot(column='engagement_rate', by='category', rot=45)
plt.title('Engagement Rate Distribution by Category')
plt.suptitle('')
plt.xlabel('Category')
plt.ylabel('Engagement Rate')
plt.tight_layout()
plt.savefig('/mnt/data/social_media_analysis_plots/engagement_rate_boxplot.png')
plt.show()

out_csv = '/mnt/data/social_media_category_analysis.csv'
df.to_csv(out_csv, index=False)

display_dataframe_to_user("Category Summary (aggregations)", agg)
display_dataframe_to_user("Top posts per category (top 3 by engagement_rate)", top_posts[[
                          'category', 'post_id', 'date', 'text_clean', 'impressions', 'likes', 'retweets', 'replies', 'engagement', 'engagement_rate']])

print(
    f"Rows before cleaning: {before}, after cleaning (removed empty text): {after}")
print(f"Saved CSV to: {out_csv}")
print("Saved plots to: /mnt/data/social_media_analysis_plots/")
