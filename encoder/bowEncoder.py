from encoder import Encoder
import numpy as np

class BowEncoder(Encoder):
    def __init__(self, sentences):
        """ Sentence encoder that encodes the sentence using Bag of Words (BOW) 

        Args:
            sentences (list): All the sentences in the poems
        """
        self.word2Idx = self.index_words(sentences)
        self.encode_dim = len(self.word2Idx)
        self.bow_matrix = self.create_bow_matrix(sentences)

    def index_words(self, sentences):
        """ To create BOW encoding, we need to first map each unique word into a index.

        Args:
            sentences (list): sentences to index  

        Returns:
            dict: Dictionary that map a word to an index
        """
        word2Idx = {}
        idx = 0
        for sentence in sentences:
            for word in sentence:
                if word not in word2Idx:
                    word2Idx[word] = idx
                    idx += 1
        return word2Idx

    def create_bow_matrix(self, sentences):
        """ For each of the sentence in the poem, encode the sentence into BOW vector and create 
        a matrix of the BOW vector so that we can use matrix multiplication to find the sentence 
        that is has highesat similarity. 

        For example, suppose there are 6 words ['I', 'love', 'have', 'am', 'good', 'you'] 

        "I love you" -> [[1 1 0 0 0 1], 
        "I am good"  ->  [1 0 0 1 1 0], 
        "I have you" ->  [1 0 1 0 0 1]]

        Args:
            sentences (list): list of sentences

        Returns:
            np.array: BOW matrix of the poems
        """
        matrix = []
        for sentence in sentences:
            matrix.append(self.encode(sentence))

        return np.stack(matrix, axis=0)


    def encode(self, sentence):
        """ Encode a sentence into BOW vector

        For example, suppose there are 6 words ['I', 'love', 'have', 'am', 'good', 'you'] in the vocabulary, 
        then the BOW vector will have a dim of 6, where each of the entry represent the frequency of the word 
        in a sentence. 

        "I love you" -> [1 1 0 0 0 1]
        "I am good"  -> [1 0 0 1 1 0] 


        Args:
            sentence (str): sentence to encode into BOW

        Returns:
            list: BOW encoding vector for the given sentence
        """
        encoding = np.zeros(self.encode_dim) 
        for word in sentence: 
            if not word in self.word2Idx: continue
            encoding[self.word2Idx[word]] += 1
        if (np.linalg.norm(encoding) != 0):
            encoding /= np.linalg.norm(encoding)
        return encoding

    def getSimilarity(self, sentence):
        """ Find the sentence in the poem that has highest similarity with the given sentence.

        Similarity is calculated by the matrix multiplication of the BOW matrix and the given
        sentence. 

        For example, suppose there are 3 sentences with 6 unique words in the poem, and we would
        like to find the most_similar sentence with "love good you"
        ['I', 'love', 'have', 'am', 'good', 'you'] 

        [BOW matrix]
        "I love you" -> [[1 1 0 0 0 1], 
        "I am good"  ->  [1 0 0 1 1 0],  
        "I have you" ->  [1 0 1 0 0 1]]

        [BOW of given sentence("love good you")]
        "love good you"
        [0 1 0 0 1 1]

        [Matrix Multiplication] 
        The result of the matrix multiplication is the similarity of the given sentence with 
        each sentence in the poems. The sentence index of the maximum is the result. 
            [[1 1 0 0 0 1], 
             [1 0 0 1 1 0],   *   [0 1 0 0 1 1]  =  [2, 1, 1]  
             [1 0 1 0 0 1]]
        First sentence has the best result. 

        Args:
            sentence (str): Sentence to find similarity

        Returns:
            int: index of the sentence in the poem that is most similar to the given sentence
                 return -1 if all the word in the given sentence are out-of-vocaulary (OOV). 
        """
        enc_sentence = self.encode(sentence)
        similarity = np.matmul(self.bow_matrix, enc_sentence) 
        return similarity