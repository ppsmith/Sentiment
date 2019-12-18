import csv

def loadCourput(tweetDataFile, trainingDataSet):
    with open(tweetDataFile, 'wt') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',', quotechar="\"")
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingDataSet

corpusFile = ""  #file path for corpus tweets

twitterFile = ""  #file path for tweet word data

loadCourput(twitterFile, corpusFile)