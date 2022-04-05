from encoder import Encoder
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class Doc2VecEncoder(Encoder):
    def __init__(self, sentences):
        self.model = self.create_model(sentences)

    def create_model(self, sentences):
        tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(sentences)]
        model = Doc2Vec(tagged_data, vector_size = 60, window = 2, min_count = 1, epochs = 100)
        return model

    def encode(self, sentence):
        return self.model.infer_vector(sentence) 

    def most_similar(self, sentence):
        sentence_vector = self.encode(sentence)
        similar_sentences = self.model.docvecs.most_similar(positive = [sentence_vector])
        print(similar_sentences)
        return similar_sentences[0][0]