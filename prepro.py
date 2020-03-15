"""
Created by: Kaushal Mamgain
Information Retreival
"""
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

def preprocess(data):                    #This function performs the preprocessing and tokenize the data
    clean = re.compile('<.*?>')         # Remove the tags
    new= re.sub(clean, '', data)
    new = new.lower()                   # Convert the data to lower case
    new = re.sub(r'[^\w\s]','',new)     # Remove the punctuations
    new = re.sub(r'[0-9]','',new)       # Remove all Digits
    new = new.split()                   # Remove white spaces
    stopWords = set(stopwords.words('english')) # Remove stop words.
    filtered = []
    for w in new:
        if w not in stopWords:
            filtered.append(w)
    #print(filtered)
    tokens = []                         # Remove all the words of length less than 3.
    for w in filtered:
        if len(w)>2:
            tokens.append(w)   
    #print(tokens)
    
    ps = PorterStemmer()                # Stem the Data.
    ps_data=[ps.stem(x) for x in tokens]
    #print(ps_data)
    stopWords = set(stopwords.words('english')) #Again look for stop wordsand remove them.
    new_filtered = []
    for w in ps_data:
        if w not in stopWords:
            new_filtered.append(w)
    return(new_filtered)                #Return the preprocessed data.