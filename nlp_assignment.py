## 1. Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.
## 2. Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume.

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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

##### PART ONE #####
sorted_df = volume_topic_df.sort_values("Volume", ascending=False)
# print(sorted_df)
top10 = sorted_df[:10]
# print(top10)
df = pd.DataFrame(top10, columns=["Topic", "Volume"])
# print(df)

df.plot.bar(x="Topic", y="Volume", legend=False)
plt.gcf().tight_layout()
plt.show()

##### PART TWO #####
greater_20000 = sorted_df[sorted_df["Volume"] > 20000]
cloud_df = pd.DataFrame(greater_20000, columns=["Topic", "Volume"])
# print(cloud_df.shape)

text = " ".join(review for review in cloud_df["Topic"].astype(str))
# print(text)

wordcloud = WordCloud(
    colormap="cool", background_color="black", width=800, height=400
).generate(text)

wordcloud = wordcloud.to_file("Topic_TweetVolume.png")
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
