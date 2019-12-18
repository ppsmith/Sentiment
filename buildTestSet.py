
def buildTestSet(keyword, twitter_api):
    try:
        tweets_fetched = twitter_api.GetSearch(keyword, count=100)  #Get 100 tweets with that contain the keyword given

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + keyword)  #print the tweet info

        return [{"text": status.text, "label": None} for status in tweets_fetched]  #return an vector with the tweet text and a label space that is blank
    except:
        print("Unfortunately, something went wrong..")
        return None