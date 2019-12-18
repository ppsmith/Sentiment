import nltk


def buildVocabSet(preprocessedTrainginData):  #function used for creating a ditribution of words used in Training Data and returns a hash of those words
    all_words = []  #list of words

    for (words, sentiment) in preprocessedTrainginData:  #put the words from the training set into the list
        all_words.extend(words)

    wordlist = nltk.FreqDist(all_words)   #generate a frequency distribution of the words in the list

    print(wordlist)

    word_features = wordlist.keys()  #create hashes of the word freq.

    return word_features  #return the hahses of the freuencies

