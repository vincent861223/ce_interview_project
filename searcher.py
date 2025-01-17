from lib2to3.pgen2.tokenize import tokenize
from telnetlib import DO
import numpy as np
import nltk
import re
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from encoder.doc2VecEncoder import Doc2VecEncoder
from encoder.bowEncoder import BowEncoder
from encoder.sentBertEncoder import SentBertEncoder

class Searcher: 

    def __init__(self, filename):
        """ The searcher class create a corpus based on the input poem file and provides API to 
        search for a similar sentence in the poem.

        Args:
            filename (str): The input file path for the poem file.
        """
        self.sentences = self.load_sentences(filename)
        self.tokenized_sentences = []
        for sentence in self.sentences:
            self.tokenized_sentences.append(self.tokenize(sentence))
        self.encoder1 = BowEncoder(self.tokenized_sentences)
        self.encoder2 = Doc2VecEncoder(self.tokenized_sentences)
        self.weight_bow = 0.6


    def load_sentences(self, filename):
        """ Load sentence from the file and return the preprocessed sentence

        Args: filename (str): The input file path for the poem file.

        Returns: : _description_
        """
        sentences = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                if (len(line) > 0): 
                    sentences.append(line)

        return sentences

    def preprocess_sentence(self, sentence):
        """ Preprocess the sentece by removing the special characters.

        Args:
            sentence (str): Sentence to preprocess

        Returns:
            str: Sentence after preprocessed
        """
        sentence = sentence.lower()
        return re.sub('[^A-Za-z0-9 ]+', ' ', sentence)
                
    def tokenize(self, sentence):
        """ Tokenize the sentence.

        Args:
            sentence (str): Sentence to tokenize

        Returns:
            list: list of words after tokenized
        """
        sentence = self.preprocess_sentence(sentence)
        return word_tokenize(sentence)


    def search(self, sentence):
        """ Search for a similar sentence in the poems for a given sentence.

        Args:
            sentence (str): Sentence to search for

        Returns:
            str: The sentence that is most similar to the given sentence
        """
        sentence = self.tokenize(sentence)
        similarity1 = self.encoder1.getSimilarity(sentence) 
        similarity2 = self.encoder2.getSimilarity(sentence)
        idx = np.argmax(self.weight_bow * similarity1 + (1-self.weight_bow) * similarity2)
        return self.sentences[idx] 