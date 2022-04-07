## Introduction
The purpose of this project is to test an applicant's coding and software design abilities. To that end, you may use online documentation and resources just as you would in your day-to-day work. This project is designed to be completed within a few hours.

## Project Story

The customer occasionally remembers a few words from a poem they once memorized.  When this happens they'd like help identifying the exact line that they are distantly recalling.  Included in this repository is [lepanto.txt](lepanto.txt), the text of a poem by G.K. Chesterton.  Your task is to write a program that prompts the user to enter the words they remember, then prints the line of the poem which you believe is the most likely match.

Here's what a hypothetical session might look like:

```
$ ./my_solution
>his head a flag
Holding his head up for a flag of all the free.
```

How you implement the "match" model is up to you but be prepared to justify the choices you make.  Assume the user doesn't have perfect recall and will confuse words from different lines on occasion.

## Assumption
1. Special character does not affect the search of a similar sentence. 


## How to run the code
### Using virtual environment
```
virtualenv venv
pip install -r requirements.txt
python my_solution.py
```

### Without virtual environment
```
pip install -r requirements.txt
python my_solution.py
```

## Implementation Notes
### BOW
Similarity is calculated by the matrix multiplication of the BOW matrix and the given sentence. 
```
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
```
* Pros: 
1. Simple to implement.
2. Fast in calculation.
* Cons: 
1. Spase matrix, hard to scale up to large corpus. 
2. If not any of the input word is in the poem, no result would be returned. 


## Example Test Cases
```
> his head a flag

> shadow yawning laughing

> black purple

> going to the war

> went war

> running on the golds

> run on the gold

```

## Reference

* [BERT For Measuring Text Similarity](https://towardsdatascience.com/bert-for-measuring-text-similarity-eec91c6bf9e1)
* [Top 4 Sentence Embedding Techniques using Python!](https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/)

* [Conceptual document similarity with word embeddings](https://investigate.ai/text-analysis/document-similarity-using-word-embeddings/)

* [Text similarity using Word2Vec](https://stackoverflow.com/questions/65852710/text-similarity-using-word2vec)

* [Doc2Vec — Computing Similarity between Documents](https://medium.com/red-buffer/doc2vec-computing-similarity-between-the-documents-47daf6c828cd)
