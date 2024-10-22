import math
from collections import defaultdict

class TF_IDF:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_scores = self.compute_tf(corpus)
        self.idf_scores = self.compute_idf(corpus)
        self.global_vocab = self.build_global_vocab(corpus)
        
    def compute_tf(self, corpus):
        # Tính toán TF
        tf_scores = []
        for doc in corpus:
            words = doc.lower().split()
            word_count = defaultdict(int)
            for word in words:
                word_count[word] += 1
            tf = {word: count / len(words) for word, count in word_count.items()}
            tf_scores.append(tf)
        return tf_scores

    def compute_idf(self, corpus):
        # Tính toán IDF
        N = len(corpus)
        word_doc_count = defaultdict(int)
        
        for doc in corpus:
            words = set(doc.lower().split())
            for word in words:
                word_doc_count[word] += 1
        
        idf = {word: math.log(N / count) for word, count in word_doc_count.items()}
        return idf

    def build_global_vocab(self, corpus):
        # Tạo từ điển toàn cục
        global_vocab = set()
        for doc in corpus:
            words = doc.lower().split()
            global_vocab.update(words)
        return list(global_vocab)
    
    def compute_tf_idf(self, max_len = None):
        # Tính toán TF-IDF
        tf_idf_vectors = []
        for doc_tf in self.tf_scores:
            tfidf_vector = [doc_tf.get(word, 0) * self.idf_scores.get(word, 0) for word in self.global_vocab]
            if max_len !=None:
                if max_len < len(self.global_vocab):
                    tfidf_vector = tfidf_vector[:max_len]
                else:
                    tfidf_vector = tfidf_vector + ([0]*(max_len - len(self.global_vocab)))
            tf_idf_vectors.append(tfidf_vector)
        print("Kích thước vecto ban đầu là: {len}", len(self.global_vocab))
        return tf_idf_vectors
    
    def encode_new_document(self, doc):
        words = doc.split()
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        tf = {word: count / len(words) for word, count in word_count.items()}
        
        tf_idf_vector = [tf.get(word, 0) * self.idf_scores.get(word, 0) for word in self.global_vocab]
        return tf_idf_vector
