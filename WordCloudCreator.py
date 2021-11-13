# This program is created for creating word clouds for Linkedin

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import STOPWORDS, WordCloud

# Reads 'linkedin_words.csv' file
df = pd.read_csv(r"linkedin_words.csv", encoding="latin-1")

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.CONTENT:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width=1584, height=396,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20, max_font_size=150).generate(comment_words)

# plot thedsad WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
