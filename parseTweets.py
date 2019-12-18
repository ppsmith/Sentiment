from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
import re

class PreProcessTweets():
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['@_USER', 'URL'])

    def processTweets(self, list_of_tweets):
        processedTweets = []
        for tweet in list_of_tweets:
            processedTweets.append((self._processTweet(tweet["text"]), tweet["label"]))
        return processedTweets

    def _processTweet(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub('((www\\.[^\\s]+)|(https?://[^\\s]+))', 'URL', tweet)
        tweet = re.sub('@[^\\s]+', 'AT_USER', tweet)
        tweet = re.sub(r'#([^\\s]+)', r'\1', tweet)
        tweet = word_tokenize(tweet)
        return [word for word in tweet if word not in self._stopwords]
