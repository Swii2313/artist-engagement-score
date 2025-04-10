# artist-engagement-score
# 🎧 Emerging Artist Scoring Model

This project aims to identify and rank **emerging music artists** using engagement metrics like monthly streams, reposts, playlist adds, and follower growth.

---

## 📊 Objective

To build a scoring model that helps discover rising music talent by assigning a weighted score based on engagement metrics.


## 🛠 Tools & Technologies

- Python (Pandas, NumPy, Matplotlib)
- CSV dataset (simulated)
- Tableau / Power BI (optional for dashboards)

## 📁 Dataset Features

Each record includes:
- Artist ID
- Month
- Monthly Streams
- Likes
- Reposts
- Playlist Adds
- Follower Growth

## 🔧 Steps Performed

1. **Data Loading** – Loaded a 3-month dataset of 30 artists.
2. **Data Cleaning** – Filled missing values using median, capped outliers using 99th percentile.
3. **Scoring Formula** – Applied weighted scoring:
4. **Ranking** – Averaged score per artist and ranked them.
5. **Visualization** – Plotted top 10 emerging artists using Matplotlib.
6. **Export** – Cleaned dataset saved for use in Tableau / Power BI dashboards.



