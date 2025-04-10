
# Emerging Artist Scoring Model - Advanced Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_csv("C:\\Users\\MYDEK\\Downloads\\Emerging_Artist_Data.csv")

# Step 2: Inspect the data
print("Initial Dataset Info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# Step 3: Data Cleaning
# Fill missing values with median of each column
df['Monthly_Streams'].fillna(df['Monthly_Streams'].median(), inplace=True)
df['Likes'].fillna(df['Likes'].median(), inplace=True)
df['Playlist_Adds'].fillna(df['Playlist_Adds'].median(), inplace=True)

# Remove outliers: Cap at 99th percentile
for col in ['Monthly_Streams', 'Likes', 'Playlist_Adds']:
    upper_limit = df[col].quantile(0.99)
    df[col] = np.where(df[col] > upper_limit, upper_limit, df[col])

# Step 4: Calculate Engagement Score
df['Engagement_Score'] = (
    0.5 * df['Monthly_Streams'] +
    0.3 * df['Playlist_Adds'] +
    0.2 * df['Reposts']
)

# Step 5: Average Score Per Artist
artist_avg = df.groupby('Artist_ID')['Engagement_Score'].mean().reset_index()
artist_avg = artist_avg.sort_values(by='Engagement_Score', ascending=False)

# Step 6: Top 10 Artists Visualization
top_10 = artist_avg.head(10)
plt.figure(figsize=(10,6))
plt.bar(top_10['Artist_ID'], top_10['Engagement_Score'], color='skyblue')
plt.title("Top 10 Emerging Artists by Engagement Score")
plt.xlabel("Artist ID")
plt.ylabel("Engagement Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 7: Export final dataset for dashboard tools
df.to_csv("Final_Cleaned_Artist_Data.csv", index=False)
print("\nCleaned and Scored data exported successfully.")
