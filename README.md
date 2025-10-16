# Social Media Post Category Analysis 📊

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python) ![Pandas](https://img.shields.io/badge/Pandas-2.x-green?logo=pandas) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green)

Welcome to the **Social Media Post Category Analysis** project! 🚀 This is an entry-level data analysis project simulating the role of a data analyst at a social media marketing agency. Think of it like building an analytics dashboard for a web app, but for social media posts. We dive into a dataset (synthetic or real via Twitter/X API) to analyze how different post categories (e.g., fitness, tech, food, beauty) perform in terms of engagement and impressions, helping marketing teams optimize their content strategy.

## 📋 Project Overview
As a web dev, imagine you’re tasked with analyzing API logs to optimize a website’s performance. This project does the same for social media, answering questions like:
- 📈 Which post categories get the most likes, retweets, or replies?
- 🕒 When should we post to maximize engagement?
- 🧠 What’s the sentiment behind top-performing posts?
- ⚠️ Are there any data anomalies affecting our insights?

The pipeline is fully automated with Python, using **Pandas** for data crunching, **Matplotlib** for visualizations, and **Jupyter** for interactive analysis. It’s like building a Node.js backend with Chart.js for a reporting tool!

## 🗃️ Dataset
The dataset (`social_media_category_analysis.csv`) is synthetic for this demo but can be replaced with real Twitter/X data. It includes ~1,000 posts with fields:
- **category**: Post category (e.g., fitness, tech, food, beauty, travel, finance, family).
- **timestamp**: Post creation time (like `created_at` in a DB).
- **text**: Post content.
- **impressions**: Number of views (null in synthetic data, estimated via median).
- **likes**: Number of likes.
- **retweets**: Number of retweets.
- **replies**: Number of replies.
- **followers_at_post**: Follower count at post time.

📂 The dataset is stored in `social_media_category_analysis.csv`, and plots are saved in `social_media_analysis_plots/`.

## 🛠️ Environment Requirements
To run this project, you need:
- **Python**: 3.12.x or compatible (e.g., 3.10+) 🐍
- **System**: Linux, macOS, or Windows (WSL works great) 💻
- **Dependencies** (in `requirements.txt`):
  - `pandas>=2.2.0`: Data manipulation, like an ORM for tables.
  - `numpy>=1.26.0`: Math operations, like Lodash for numbers.
  - `matplotlib>=3.8.0`: Plotting, like Chart.js for viz.
  - `tweepy>=4.14.0`: For Twitter/X API integration (optional).
  - `jupyter>=1.0.0`: Notebook server, like a dev server for analysis.

## ⚙️ Setup Instructions
Follow these steps to set up the project, like initializing a Node.js app with `npm install`:

1. **Clone the Repository** 📥:
   ```bash
   git clone https://github.com/binhchay1/social-media-category-analysis.git
   cd social-media-category-analysis
   ```

2. **Download the Dataset** 📂:
   - The synthetic dataset (`social_media_category_analysis.csv`) is included.
   - For real Twitter/X data, set up the Twitter API v2 (see **Integration with Twitter/X API** below).

3. **Create a Virtual Environment** 🏗️:
   Avoid conflicts (e.g., `externally-managed-environment` error on Debian):
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment** 🔄:
   ```bash
   # Linux/macOS
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```
   Your prompt should show `(venv)`.

5. **Install Dependencies** 📦:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. **Register Jupyter Kernel** 🔗:
   Link the virtual environment to Jupyter:
   ```bash
   python -m ipykernel install --user --name=social-media-analysis --display-name="Social Media Analysis (Python 3.12)"
   ```

## 🚀 How to Run
1. **Start Jupyter Notebook** 🌐:
   ```bash
   jupyter notebook main_analysis.ipynb
   ```
   Open the browser, select `main_analysis.ipynb`, and choose the "Social Media Analysis (Python 3.12)" kernel.

2. **Run All Cells** ▶️:
   - Click "Run All" in Jupyter or execute cells sequentially.
   - Outputs include data summaries, visualizations (bar, scatter, line, boxplot), and insights.

3. **Deactivate Environment** 🛑:
   ```bash
   deactivate
   ```

## 📁 Project Structure
Like a web app repo, here’s the layout:
```
social-media-category-analysis/
├── social_media_category_analysis.csv  # Dataset (synthetic or real) 📂
├── social_media_analysis_plots/        # Generated plots, like a dist/ folder 📈
│   ├── avg_engagement_rate_by_category.png
│   ├── impressions_vs_engagement_rate.png
│   ├── posting_volume_7dayma.png
│   └── engagement_rate_boxplot.png
├── main_analysis.ipynb                 # Core notebook, like src/ for code 📓
├── requirements.txt                    # Dependencies, like package.json 📋
├── .gitignore                         # Excludes venv/, plots/, etc. 🚫
├── README.md                          # You're reading it! 📖
└── LICENSE                            # MIT License 📜
```

## 📈 Key Findings (Synthetic Data)
Running `main_analysis.ipynb` yields:
- **Top Category**: Food (~3.5% engagement rate, 220 posts) 🍔
- **Consistent Performer**: Beauty (~3.2% engagement rate, consistent across posts) 💄
- **High Impressions**: Tech (~2.1% engagement rate, high views but moderate engagement) 💻
- **Time-Sensitive**: Travel (~2.0% engagement rate, spiky based on posting time) ✈️
- **Engagement Formula**: `engagement = likes + retweets + replies`, `engagement_rate = engagement / impressions`.
- **Notes**: Short posts with hashtags drive higher engagement in Food and Beauty.

📊 **Visualizations**:
- Bar chart: Average engagement rate by category.
- Scatter plot: Impressions vs. engagement rate.
- Line chart: Posting volume (7-day moving average).
- Boxplot: Engagement rate distribution by category.

## 💡 Recommendations
Like optimizing a web app based on analytics:
- **Content Strategy**: Focus on Food and Beauty posts for high engagement 🍽️💅
- **Posting Schedule**: Post Travel content during peak seasons (e.g., holidays) ✈️
- **Hashtags**: Use 2-3 targeted hashtags to boost visibility (like SEO for posts) 🔗
- **Sentiment**: Prioritize positive-tone posts for better engagement (use sentiment analysis) 😊
- **Real Data**: Switch to Twitter/X API for live insights (see below) 🌐

## 🔄 Integration with Real Twitter/X API
To use real Twitter/X data, replace the synthetic data block in `main_analysis.ipynb` with:
```python
import tweepy
import pandas as pd

client = tweepy.Client(bearer_token="YOUR_TWITTER_BEARER_TOKEN")
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
        "impressions": None,  # Impressions not available in public API
        "language": t.lang,
        "category": "fitness"  # Classify by hashtag
    })
df = pd.DataFrame(rows)
```

## 🛠️ Troubleshooting
- **Error: `externally-managed-environment`** ⚠️: Ensure you’re in the virtual environment (`source venv/bin/activate`). Check `which pip` points to `venv/bin/pip`.
- **Module Not Found** 🚫: Reinstall dependencies (`pip install -r requirements.txt`) or specific packages (`pip install pandas`).
- **Jupyter Not Launching** 🌐: Check port 8888 (`jupyter notebook --port=8889` if blocked).
- **Twitter API Errors** 🔒: Verify bearer token and API rate limits (Twitter/X API v2).

## 🤝 Contributing
Feel free to fork, submit PRs, or open issues! Treat it like contributing to an open-source Python package. 🌟

## 📜 License
MIT License (see `LICENSE`).

## 📞 Contact
- **Author**: Thanh Bình Nguyễn
- **Role**: Data Analyst
- **Email**: binhchay1@gmail.com
- **GitHub**: [github.com/binhchay1](https://github.com/binhchay1)
Got questions? Open an issue at [github.com/binhchay1/social-media-category-analysis/issues](https://github.com/binhchay1/social-media-category-analysis/issues).
