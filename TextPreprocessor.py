import pandas as pd
import re
from pyvi import ViTokenizer

EMAIL = re.compile(r"([\w0-9_\.-]+)(@)([\d\w\.-]+)(\.)([\w\.]{2,6})")
URL = re.compile(r"http\S+|www\S+|https\S+")
PHONE = re.compile(r"(09|01[2|6|8|9])+([0-9]{8})\b")
MENTION = re.compile(r"@.+?:")
NUMBER = re.compile(r"\d+.?\d*")
DATETIME = '\d{1,2}\s?[/-]\s?\d{1,2}\s?[/-]\s?\d{4}'
NON_ALPHANUMERIC = re.compile(r'[^\w\s]')
SINGLE_LETTERS = re.compile(r'\s+[a-zA-Z]\s+')



class TextPreprocessor:
    def __init__(self, stopwords_file):
        self.stopword_set = self.load_stopwords(stopwords_file)

    def load_stopwords(self, stopwords_file):
        stopword_df = pd.read_csv(stopwords_file, header=None, names=['stopword'])
        return set(stopword_df['stopword'])

    def remove_stopwords(self, line):
        words = [] 
        for word in line.strip().split(): 
            if word not in self.stopword_set:
                words.append(word)
        return ' '.join(words)
    
    def replace_common_token(self, text):
        text = re.sub(EMAIL, ' ', text)
        text = re.sub(URL, ' ', text)
        text = re.sub(MENTION, ' ', text)
        text = re.sub(DATETIME, ' ', text)
        text = re.sub(NUMBER, ' ', text)
        text = re.sub(NON_ALPHANUMERIC, ' ', text)
        text = re.sub(SINGLE_LETTERS, ' ', text)
        return text
    
    def remove_emoji(self, text):
        text = re.sub(r':v', '', text)
        text = re.sub(r':D', '', text)
        text = re.sub(r':3', '', text)
        text = re.sub(r':\(', '', text)
        text = re.sub(r':\)', '', text)
        return text

    
    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'&.{3,4};', ' ', text)
        text = self.remove_emoji(text)
        text = self.replace_common_token(text)
        text = ViTokenizer.tokenize(text)
        text = self.remove_stopwords(text)
        return text

    def preprocess_data(self, df):
        df['text'] = df['text'].apply(self.preprocess_text)
        return df
