import csv
import twitter
import time

twitter_api = twitter.Api(consumer_key="", consumer_secret="",
                          access_token_key="", access_token_secret="")  #loggin in credentials,need to get your own

corpusFile = "C:\\Users\\ppsmith\\Documents\\twitter-sentiment-training-master\\twitter-sentiment-training-master\\corpus.csv"  #file path for corpus tweets

twitterFile = "C:\\Users\\ppsmith\\Documents\\twitterData\\tweetDataFile.csv"  #file path for tweet word data

def buildTrainingSet (corpusFile, tweetDataFile):  #download the dataset
    corpus = []  #will hold the tweet data

    with open(corpusFile, 'rt') as csv_file:
        linereader = csv.reader(csv_file, delimiter = ',', quotechar = "\"")  #open a line reader to scan the contents of the file

        for row in linereader:
            corpus.append({"tweet_id": row[2], "label": row[1], "topic": row[0]})  #add row titles

    rate_limit = 180  #twitter API's limit the rate at which tweets can be downloaded, this function ensures that the rate is met
    sleep_time = 900 / 180

    trainingDataSet = []  #list of tweets with the actual "tweet" string
    i = 0
    for tweet in corpus:
        try:
            #if( i == 5): break;
            status = twitter_api.GetStatus(tweet["tweet_id"])  #tell twitter to get the tweet associated with the tweetID
            print("Tweet fetched", i)
            i = i + 1
            tweet["text"] = status.text  #the text of tweet is the test of the tweet from twitter
            trainingDataSet.append(tweet)  #add the tweet test to the data set
            time.sleep(sleep_time)  #wait, ensures we are not trying to et new tweets too fast
        except:
            continue
    return trainingDataSet


buildTrainingSet(corpusFile, twitterFile)