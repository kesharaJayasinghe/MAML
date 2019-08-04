# Edited Python script used in the predict sentiment experiment. 
# To work with the web service (Sentiment Analysis Demo)
# Source: Microsoft - Introduction to Artificial Intelligence (AI) course

import pandas as pd

def azureml_main(dataset, stop_words);
    import os
    import pandas as pd
    import string
    import nltk
    from nltk.stem.porter import PorterStemmer
    
    # Give the columns names and make a list of the tweets
    dataset.columns = ['tweets']
    tweets = dataset['tweets'].tolist()
    
    # For each tweet, remove punctuation and set to lower case
    sp = string.punctuation
    tweets = list(map(lambda t: ''.join(["" if c.isdigit() else c for c in t]), tweets))
    tweets = list(map(lambda t: ''.join(["" if c in sp else c for c in t]), tweets))
    tweets = list(map(str.lower, tweets))
    
    # Stem the tweet text
    porter_stemmer = PorterStemmer()
    temp = [tweet.split() for tweet in tweets]      # Split tweets into tokens
    tweets = list(map(lambda t: ' '.join([porter_stemmer.stem(word) for word in t.split()]), tweets))
    
    # Remove stop words
    stop_words = [w for w in stop_words.words if w in stop_words.words.unique()]
    tweets = list(map(lambda t: ' '.join([word for word in t.split() if word not in set(stop_words)]), tweets))
    
    
    
