import re
import random
import sys
from collections import defaultdict


def words(filename):
        
        with open(filename, 'r') as f:
                raw = f.read()

        # strip non-words and most punctuation, fix caps
        words = [capitals(w) for w in re.findall(r"[\w']+|[.,!?;]", raw)] 

        return words


def capitals(word):
    
        if word.isupper() and word != "I":
                word = word.lower()
    
        elif word[0].isupper():
                word = word.lower().capitalize()
        
        else:
                word = word.lower()
    
        return word

# Building and normalizing the mapping.
def make_graph(wordlist, n):
    
        starts = []
        starts.append(wordlist[0])
        graph = defaultdict(int)

        for i in range(1, len(wordlist)-1):

                if i <= n:
                        history = wordlist[:i+1]

                else:
                        history = wordlist[i-n+1:i+1]

                follow = wordlist[i+1]                
                               
                graph[' '.join(history)] += 1
 
                if history[-1] == "." and follow not in ".,!?;":
                        starts.append(follow)
        
        return graph

# Returns the next word in the sentence (chosen randomly),
# given the previous ones.
def next_random(prev):

        

def get_sentence(starts, graph, n):

        # Start with a random "starting word"
        curr = random.choice(starts)
        sent = curr.capitalize()
    
        prev = [curr]
        # Keep adding words until we hit punctuation
        while (curr not in "!?."):
                
                curr = next(prevList)
                prevList.append(curr)
        
        # if the prevList has gotten too long, trim it
        if len(prevList) > markovLength:
                prevList.pop(0)
        
        if (curr not in ".,!?;"):
            sent += " " # Add spaces between words (but not punctuation)
        
        sent += curr
    
        return sent


if __name__ == '__main__':

        filename = 'messages.txt'
        n_gram_length = 3

