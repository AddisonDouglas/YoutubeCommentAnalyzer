import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sys
import seaborn as sns
import matplotlib.pyplot as plt
nltk.download('punkt')
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
df = pd.read_csv('output.csv')
df['index'] = range(1, len(df) + 1)
res = {}
for index, row in df.iterrows():
    res[row['index']] = sia.polarity_scores(row.iloc[0])


sentiment = pd.DataFrame(res).T

sentiment['index'] = range(1, len(sentiment) + 1)
sentiment = sentiment.merge(df, how = 'left')
print(sentiment.to_string())
ax = sns.barplot(data = sentiment, y = 'compound', x = 'index' )
plt.show()