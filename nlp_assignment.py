## 1. Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.
## 2. Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume.

from textblob import TextBlob
from pathlib import Path
import pandas as pd
from operator import itemgetter

from nyc_trends import nyc_trends

tweets = nyc_trends[0]["trends"]
print(len(tweets))

volume = tweets[0]["tweet_volume"]
print(volume)

"""
list_of_tweets = nyc_trends["trends"]
print(len(list_of_tweets))


sorted_text = sorted(tweet_volume)
top10 = sorted_text[:10]
print(top10)
"""
