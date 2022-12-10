import pandas as pd
import numpy as np
import re
import string
import contractions
import collections
from datetime import datetime
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import tweepy
import config


class TextVectors():

    """
    Class to manage the TFIDVectorizer across models 
    Initialize with a dataframe containing text.
    Creates an object with "create_vectorized_text" as a method.
    """

    def __init__(self, df, training = False, config=config):
        self.stop_words = nltk.corpus.stopwords.words('english')
        self.df = df
        self.tfid_vec = TfidfVectorizer(ngram_range=(1,2), lowercase=True, min_df = 1)
        if training == True: self.train_vectorizer(self.df)

    def train_vectorizer(self, df):
        # sets the initial vectorized training data to self.vector_X
        X = df['text'].apply(lambda x: self.preprocess_text(x, flg_stemm=True, flg_lemm=True, lst_stopwords=self.stop_words))
        self.vector_X =  self.tfid_vec.fit_transform(X)

    def produce_additional_vectors(self, df):
        # new text is vectorized using the same TFIDVectorize object but transformed
        X = df['text'].apply(lambda x: self.preprocess_text(x, flg_stemm=True, flg_lemm=True, lst_stopwords=self.stop_words))
        new_vector_X =  self.tfid_vec.transform(X)
        return new_vector_X

    def preprocess_text(self, text, flg_stemm = True, flg_lemm = True, lst_stopwords=None):
        # function to control the processing of the text itself 
        text_clean = re.sub(r'[^\w\s.,]', '', str(text).strip())
        lst_text = text_clean.split()
        if lst_stopwords is not None:
            lst_text = [word for word in lst_text if word not in lst_stopwords]
        if flg_stemm == True:
            stemm = nltk.stem.porter.PorterStemmer()
            lst_text = [stemm.stem(word) for word in lst_text]
        if flg_lemm == True:
            lem=nltk.stem.wordnet.WordNetLemmatizer()
            lst_text = [lem.lemmatize(word) for word in lst_text]
        text_clean = ' '.join(filter(None, lst_text))
        text_clean = text_clean.replace(" ,",",").replace(' .', '.')
        text_clean = contractions.fix(text_clean)
        return text_clean

    def __call__(self, df):
        # call on new dataframes
        vectors = self.produce_additional_vectors(df)
        return vectors
