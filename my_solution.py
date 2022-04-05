from searcher import Searcher


def cli(searcher):
    while True:
        sentence = input('> ') 
        if sentence.lower() == 'exit': exit(0)
        print(searcher.search(sentence))


if __name__ == '__main__':
    searcher = Searcher('lepanto.txt')
    cli(searcher)