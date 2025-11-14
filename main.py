import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "./data/movies_metadata.csv"
df = pd.read_csv(url)
# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())
# print(df.belongs_to_collection)
# print(df[["belongs_to_collection", "homepage", "tagline"]])
# print(df.tagline)
# df[["belongs_to_collection", "homepage", "tagline"]]
# df["tagline"].fillna("without tagline", inplace=True)
# df.fillna({"tagline": "without tagline"}, inplace=True)
df["tagline"] = df["tagline"].fillna("without tagline")
# print(df.tagline)
df["homepage"] = df["homepage"].fillna("No homepage")
# print(df.homepage)
df["belongs_to_collection"] = df["belongs_to_collection"].fillna("{}")
# print(df.belongs_to_collection)
# df.info()
df.dropna(inplace=True)
# print(df.isnull().sum())
# df.info()

# print(df.genres)
genres_count = df["genres"].value_counts()
# print(genres_count)
# print(genres_count.index)
# print(genres_count.values)

plt.figure(figsize=(10,6))

sns.barplot(x=genres_count.index, y=genres_count.values)

plt.title("Count of genres")
plt.xlabel("Genres")
plt.ylabel("Counts")

plt.xticks(rotation=45)

plt.show()