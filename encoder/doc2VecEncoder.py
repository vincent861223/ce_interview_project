from encoder import Encoder
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class Doc2VecEncoder(Encoder):
    def __init__(self, sentences):
        self.model = self.create_model(sentences)
        self.n = len(sentences)

    def create_model(self, sentences):
        tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(sentences)]
        model = Doc2Vec(tagged_data, vector_size=60, epochs=100)
        return model

    def encode(self, sentence):
        return self.model.infer_vector(sentence) 

    def getSimilarity(self, sentence):
        similarity = np.zeros(self.n) 
        sentence_vector = self.encode(sentence)
        similar_sentences = self.model.docvecs.most_similar(positive=[sentence_vector], topn=self.n)
        for idx, sim in similar_sentences: 
            similarity[idx] = sim

        return similarity