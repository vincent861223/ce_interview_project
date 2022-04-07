from encoder import Encoder
import numpy as np
from sentence_transformers import SentenceTransformer

class SentBertEncoder(Encoder):
    def __init__(self, sentences):
        print('Loading pretrained sentenceBERT model...')
        self.model = SentenceTransformer('bert-base-nli-mean-tokens') 
        self.bow_matrix = self.create_bow_matrix(sentences)

    def create_bow_matrix(self, sentences):
        print('Creating sentence matrix...')
        matrix = []
        for sentence in sentences:
            enc = self.encode(sentence) 
            matrix.append(enc)

        return np.stack(matrix, axis=0)

    def encode(self, sentence):
        sentence = " ".join(sentence)
        enc = self.model.encode(sentence) 
        print(enc.shape)
        if (np.linalg.norm(enc) != 0):
            enc /= np.linalg.norm(enc)
        return enc
    
    def most_similar(self, sentence):
        enc_sentence = self.encode(sentence)
        similarity = np.matmul(self.bow_matrix, enc_sentence) 
        return similarity