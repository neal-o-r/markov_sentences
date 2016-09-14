import re
import random
from tqdm import tqdm
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
    
        else:
                word = word.lower()
    
        return word


def make_graph(wordlist, n):
    
        starts = []
        starts.append(wordlist[0])
        graph = defaultdict(list)

        for i in tqdm(range(len(wordlist)-n)):

                history = tuple(wordlist[i:i+n+1])
                               
                for i in range(len(history)):

               	 	h = history[:i]
                	follow = history[i]
                 
                        
                	graph[h].append(follow) 
                
                if "." == history[-2] and history[-1] not in ".?!,":
				
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
        sent = curr.capitalize() 
    
        prev = [curr]
        # Keep adding words until we hit punctuation
        while (curr not in "!?."):
                
                connections = get_connections(prev, graph, n)
                curr = random.choice(connections) 
                prev.append(curr)
                 
                if (curr not in ".,!?;"):
                        sent += " " # Add spaces between words (but not punctuation)
        
                sent += curr
    
        return sent


if __name__ == '__main__':

        filename = 'pota.txt'
        n_gram_length = 2

        starts, graph = make_graph(words(filename), n_gram_length)

        for i in range(10):
                print(get_sentence(starts, graph, n_gram_length))
