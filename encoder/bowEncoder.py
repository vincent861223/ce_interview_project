from encoder import Encoder
import numpy as np

class BowEncoder(Encoder):
    def __init__(self, sentences):
        self.word2Idx = self.index_words(sentences)
        self.encode_dim = len(self.word2Idx)
        self.bow_matrix = self.create_bow_matrix(sentences)

    def create_bow_matrix(self, sentences):
        matrix = []
        for sentence in sentences:
            matrix.append(self.encode(sentence))

        return np.stack(matrix, axis=0)


    def encode(self, sentence):
        encoding = np.zeros(self.encode_dim) 
        for word in sentence: 
            if not word in self.word2Idx: continue
            encoding[self.word2Idx[word]] = 1

        return encoding

    def index_words(self, sentences):
        word2Idx = {}
        idx = 0
        for sentence in sentences:
            for word in sentence:
                if word not in word2Idx:
                    word2Idx[word] = idx
                    idx += 1
        return word2Idx


    def most_similar(self, sentence):
        enc_sentence = self.encode(sentence)
        similarity = np.matmul(self.bow_matrix, enc_sentence) 
        return np.argmax(similarity)