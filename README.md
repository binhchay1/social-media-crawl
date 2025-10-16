# 📊 Social Media Post Category Analysis

**Author:** Thanh Bình Nguyễn  
**Role:** Data Analyst (Entry-level project scenario)

## 🧩 Project Overview

This project simulates the role of a **data analyst** at a **social media marketing agency**.  
The goal is to analyze how different categories of social media posts (e.g., _fitness, tech, family, food, beauty, travel, finance_) perform in terms of engagement and impressions.

The final output helps marketing teams:

- Identify **which types of content** drive the most engagement.
- Optimize posting **strategies by category**.
- Make **data-driven recommendations** to improve social media performance.

The analysis pipeline is fully automated with **Python**, covering:

1. Data collection (synthetic for demo; can connect to Twitter/X API)
2. Data cleaning & preprocessing
3. Feature engineering (engagement rate, sentiment, etc.)
4. Exploratory data analysis (EDA)
5. Visualization and insights export

---

## 🧠 Project Objectives

- **Increase client reach and engagement**
- **Gain valuable insights** to guide social strategy
- **Deliver actionable recommendations** to improve performance

---

## ⚙️ Tech Stack

| Component         | Description                                      |
| ----------------- | ------------------------------------------------ |
| **Language**      | Python 3                                         |
| **Libraries**     | pandas, numpy, matplotlib, re                    |
| **Environment**   | Jupyter / VSCode Notebook                        |
| **Visualization** | Matplotlib (one plot per figure)                 |
| **Data Source**   | Synthetic dataset (can connect to Twitter/X API) |

---

## 🗂️ Project Structure

├── social_media_category_analysis.csv # Cleaned & feature-engineered dataset
├── /social_media_analysis_plots/ # Folder containing generated plots
│ ├── avg_engagement_rate_by_category.png
│ ├── impressions_vs_engagement_rate.png
│ ├── posting_volume_7dayma.png
│ └── engagement_rate_boxplot.png
├── main_analysis.ipynb # Core notebook (data processing + visualization)
└── README.md # This file

---

## 🧪 Workflow Summary

### 1. Data Generation / Collection

- In this demo, data is **synthetically generated** to simulate real-world posts.
- Each post includes fields like:
  - `category`, `timestamp`, `text`, `impressions`, `likes`, `retweets`, `replies`, `followers_at_post`
- Categories include: `fitness`, `tech`, `family`, `food`, `beauty`, `finance`, `travel`.

👉 _To replace synthetic data with real Twitter/X data_, use the [Twitter API v2](https://developer.x.com/en/docs) and the `tweepy` library (see code snippet below).

### 2. Cleaning & Preprocessing

- Removes URLs, mentions, hashtags symbols, and non-ASCII characters.
- Fills missing impressions using category median values.
- Drops empty or invalid text posts.

### 3. Feature Engineering

- `engagement` = likes + retweets + replies
- `engagement_rate` = engagement / impressions
- Adds text-based metrics: `word_count`, `hashtags_count`, `mentions_count`
- Adds simple rule-based sentiment scoring

### 4. Aggregation & Analysis

Aggregated results by category include:

- Average & median impressions
- Average engagement rate
- Average sentiment
- Word count statistics

### 5. Visualization

- 📈 **Engagement rate by category** (bar chart)
- 🔹 **Impressions vs engagement rate** (scatter plot)
- 🕒 **Posting volume over time (7-day moving average)**
- 📦 **Engagement rate distribution (boxplot)**

---

## 📊 Example Findings (synthetic data)

| Category | Avg Engagement Rate | Posts | Notes                                     |
| -------- | ------------------: | ----: | ----------------------------------------- |
| Food     |               ~3.5% |   220 | High engagement, short posts perform best |
| Beauty   |               ~3.2% |   145 | Consistent engagement across posts        |
| Tech     |               ~2.1% |   210 | High impressions, moderate engagement     |
| Travel   |               ~2.0% |   110 | Spiky engagement, time-dependent          |

_(Your results may vary with real data.)_

---

## 🔄 Integration with Real Twitter/X API

Replace the synthetic data generation block with:

```python
import tweepy
import pandas as pd

client = tweepy.Client(bearer_token=YOUR_TWITTER_BEARER_TOKEN)

query = "#fitness OR #tech OR #food lang:en -is:retweet"
tweets = client.search_recent_tweets(query=query,
                                     tweet_fields=["created_at", "public_metrics", "lang"],
                                     max_results=100)

rows = []
for t in tweets.data:
    m = t.public_metrics
    rows.append({
        "timestamp": t.created_at,
        "text": t.text,
        "likes": m["like_count"],
        "retweets": m["retweet_count"],
        "replies": m["reply_count"],
        "impressions": None,  # impressions not available in public API
        "language": t.lang,
        "category": "fitness"  # or classify by hashtag
    })
df = pd.DataFrame(rows)
```
