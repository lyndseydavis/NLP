from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)

print(blob)

# creates list of sentences
sentences = blob.sentences
print(sentences)

# creates list of words
words = blob.words
print(words)
"""
# list of words and tag (like noun, verb, etc.)
print(blob.tags)

# list of only the noun phrases
print(blob.noun_phrases)

# sentiment analysis

# subjectivity and polarity are numbers between -1 and 1
print(blob.sentiment)
# print(blob.sentiment.polarity)

# analyze sentiment polarity for each sentence
for sentence in sentences:
    print(round(sentence.sentiment.polarity, 3))

# using a different analyzer
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)
"""
# language translation and detection
spanish = blob.translate(to="es")
print(spanish)

chinese = blob.translate(to="zh")
print(chinese)

french = blob.translate(to="fr")
print(french)

hindi = blob.translate(to="hi")
print(hindi)

nepali = blob.translate(to="ne")
print(nepali)

back_to_english = nepali.translate()
print(back_to_english)
