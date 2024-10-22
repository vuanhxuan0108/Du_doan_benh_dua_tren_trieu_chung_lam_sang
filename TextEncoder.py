import numpy as np

class TextEncoder:
    def __init__(self, max_len=150):
        self.max_len = max_len
        self.word_to_id = {}
        self.unique_words = set()
        self.current_id = 1

    def process_corpus(self, corpus):
        for text in corpus:
            words = text.lower().split()
            for word in words:
                if word not in self.unique_words:
                    self.unique_words.add(word)
                    self.word_to_id[word] = self.current_id
                    self.current_id += 1
        return self.unique_words, self.word_to_id

    def encode_text(self, text):
        words = text.split()
        encoded_text = [self.word_to_id[word.lower()] if word.lower() in self.word_to_id else -1 for word in words]
        if len(encoded_text) < self.max_len:
            encoded_text = ([0] * (self.max_len - len(encoded_text))) + encoded_text
        else:
            encoded_text = encoded_text[:self.max_len]
        return encoded_text

    def fit_transform(self, corpus):
        self.process_corpus(corpus)
        return np.array([self.encode_text(sentence) for sentence in corpus])

    def transform(self, corpus):
        return np.array([self.encode_text(sentence) for sentence in corpus])

