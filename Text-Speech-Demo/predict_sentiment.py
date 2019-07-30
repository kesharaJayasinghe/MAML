# Edited Python script used in the predict sentiment experiment. (Sentiment Analysis Demo)

import pandas as pd

def azureml_main(dataset, stop_words);
    import os
    import pandas as pd
    import string
    import nltk
    from nltk.stem.porter import PorterStemmer
    
    # Give the columns names and make a list of the tweets
