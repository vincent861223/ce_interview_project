from lib2to3.pgen2.tokenize import tokenize
from telnetlib import DO

import nltk
import re
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from encoder.doc2VecEncoder import Doc2VecEncoder
from encoder.bowEncoder import BowEncoder

class Searcher: 
    def __init__(self, filename):
        self.sentences = self.load_sentences(filename)
        self.tokenized_sentences = self.tokenize_all(self.sentences)
        self.encoder = BowEncoder(self.tokenized_sentences)

    def load_sentences(self, filename):
        sentences = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                sentences.append(self.preprocess_sentence(line))

        return sentences

    def preprocess_sentence(self, sentence):
        sentence = sentence.strip('\n')
        return re.sub('[^A-Za-z0-9 ]+', '', sentence)
                
    def tokenize_all(self, sentences):
        tokenized_sentences = []
        for sentence in sentences:
            tokenized_sentences.append(self.tokenize(sentence))
        return tokenized_sentences

    def tokenize(self, sentence):
        return word_tokenize(sentence.lower())


    def search(self, sentence):
        idx = self.encoder.most_similar(self.tokenize(sentence)) 
        return self.sentences[idx] 

    def __str__(self):
        return str(self.sentences)