## 1. Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.
## 2. Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume.

from textblob import TextBlob
from pathlib import Path
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt

from nyc_trends import nyc_trends

tweets = nyc_trends[0]["trends"]
# print(len(tweets))

volume, topic = [], []
for tw in range(len(tweets)):
    vol = tweets[tw]["tweet_volume"]
    volume.append(vol)
# print(volume)

for tw in range(len(tweets)):
    name = tweets[tw]["name"]
    topic.append(name)
# print(topic)
volume_topic_dict = {"Topic": topic, "Volume": volume}
# print(volume_topic_dict)
volume_topic_df = pd.DataFrame(volume_topic_dict)
# print(volume_topic_df)

sorted_df = volume_topic_df.sort_values("Volume", ascending=False)
top10 = sorted_df[:10]
df = pd.DataFrame(top10, columns=["Topic", "Volume"])
print(top10)

df.plot.bar(x="Topic", y="Volume", legend=False)
plt.gcf().tight_layout()  # need to fix this???
plt.show()
