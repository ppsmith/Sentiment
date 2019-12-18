import twitter
import nltk
import CorpusDownload
import buildTestSet
import buildVocabSet
import parseTweets
import Extract

def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features

twitter_api = twitter.Api(consumer_key="QNU55j6Q526bMynDtIK4fRlbh", consumer_secret="fWcQHjgACPnjVsklzzKu8GF5dumTCLhexeCsKGYnjfVeKJeS7b",
                          access_token_key="619625963-f9yEnWliUjowYHEdIHAu6uNYkpBpOcUX3ITfPO7x", access_token_secret="GHIxJddFRMqETqxMqklF3R2zKevFQ9cSnkjhjgqVUfQdJ")  #log in in credentials

corpusFile = "C:\\Users\\ppsmith\\Documents\\twitter-sentiment-training-master\\twitter-sentiment-training-master\\corpus.csv"  #file path for corpus tweets

twitterFile = "C:\\Users\\ppsmith\\Documents\\twitterData\\tweetDataFile.csv"  #file path for tweet word data

trainingData = CorpusDownload.buildTrainingSet(corpusFile, twitterFile)  #the trainingData is the result of dowloading the tweets based on the info in the corpus file, and ten adding that to the twitter file

search = input("Please type in serach term: ")  #take in a search term from the user

testDataSet = buildTestSet.buildTestSet(search, twitter_api)  #the trest data is 100 tweets that contain the search term from the user

tweetProcessor = parseTweets.PreProcessTweets()  #the tweetProcessor object is an instance of the parseTweets class. The methods in the class parse the tweets

preprocessedTrainingSet = tweetProcessor.processTweets(trainingData)  #preporcessedTraingData is the 100 tweets once they have gone through the pre-processor

preprocessedTestSet = tweetProcessor.processTweets(testDataSet)  #the preprocessedTestSet is the set of corpus tweets that have gone through the pre-processor

word_features = buildVocabSet.buildVocabSet(preprocessedTrainingSet)  #word fetureas are the NLP features of the trainingset (100 tweets).

trainingFeatures = nltk.classify.apply_features(extract_features, preprocessedTrainingSet)  #traingFeature are the features of the entirs tweet set

NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)  #train on the large tweet file

NBResultLabels = [NBayesClassifier.classify(Extract.extract_features(tweet[0], word_features)) for tweet in preprocessedTestSet]  #Classify each tweet in the 100 subtweets


#generate results
if NBResultLabels.count('positive') > NBResultLabels.count('negative'):
    print("Overall Positive Sentiment")
    print(NBResultLabels.count('positive'))
    print("Positive Sentiment Percentage = " + str(100*NBResultLabels.count('positive')/len(NBResultLabels)) + "%")
else:
    print("Overall Negative Sentiment")
    print("Negative Sentiment Percentage = " + str(100*NBResultLabels.count('negative')/len(NBResultLabels)) + "%")



