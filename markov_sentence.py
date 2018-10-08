import re
import random
from collections import defaultdict
import nltk

def words(filename):
        with open(filename, 'r') as f:
                words = [capitals(w) for w in nltk.word_tokenize(f.read())]

        tagged_words = nltk.pos_tag(words)
        return tagged_words


def capitals(word):
        if word.isupper() and word != "I":
                return word.lower()
        return word.lower()


def make_graph(wordlist, n):

        starts = []
        starts.append(wordlist[0])
        graph = defaultdict(list)

        for i in range(len(wordlist)-n):

                history = wordlist[i:i+n+1]
                for j in range(len(history)):

                        h = tuple(history[:j])
                        follow = history[j]

                        graph[h].append(follow)

                if "." == history[-2][0] and history[-1][0] not in ".?!,":
                        starts.append(history[-1])

        return starts, graph


def get_connections(path, graph, n):

        state = path[-n:]
        while tuple(state,) not in graph:
                state.pop(0)

        if len(state) == 0:
                return None
        else:
                return graph[tuple(state,)]


def get_sentence(starts, graph, n):

        # Start with a random "starting word"
        curr = random.choice(starts)
        sent = curr[0].capitalize()

        prev = [curr]
        # Keep adding words until we hit punctuation
        while (curr[0] not in "!?."):

                connections = get_connections(prev, graph, n)
                curr = random.choice(connections)
                prev.append(curr)

                if (curr[0] not in ".,!?;"):
                        sent += " " # Add spaces between words (but not punctuation)

                sent += curr[0]

        return sent


if __name__ == '__main__':

        filename = 'pota.txt'
        n_gram_length = 3

        starts, graph = make_graph(words(filename), n_gram_length)

        for i in range(10):
                print(get_sentence(starts, graph, n_gram_length))
