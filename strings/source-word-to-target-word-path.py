import collections
import string

__author__ = 'dsbatista'

# http://www.ardendertat.com/2011/10/17/programming-interview-questions-8-transform-word/

"""
Given a source word, target word and an English dictionary, transform the
source word to target by changing/adding/removing 1 character at a time,
while all intermediate words being valid English words. Return the
transformation chain which has the smallest number of intermediate words.
"""


def construct_graph(dictionary):
    graph = collections.defaultdict(list)
    letters = string.lowercase
    for word in dictionary:
        for i in range(len(word)):

            # remove 1 character
            remove = word[:i]+word[i+1:]
            if remove in dictionary:
                graph[word].append(remove)

            # change 1 character
            for char in letters:
                change = word[:i]+char+word[i+1:]
                if change in dictionary and change != word:
                    graph[word].append(change)

            # add 1 character
            for x in range(len(word)+1):
                for char in letters:
                    add = word[:x]+char+word[x:]
                if add in dictionary:
                    graph[word].append(add)
    return graph


# TODO: Breadth-first
def transform_word(graph, start, goal):
    paths = collections.deque([[start]])
    extended = set()
    # Breadth First Search
    while len(paths) != 0:
        current_path = paths.popleft()
        current_word = current_path[-1]
        if current_word == goal:
            return current_path
        elif current_word in extended:
            # already extended this word
            continue

        extended.add(current_word)
        transforms = graph[current_word]
        for word in transforms:
            if word not in current_path:
                # avoid loops
                paths.append(current_path[:]+[word])

    print paths
    print extended
    # no transformation
    return []


def main():
    #dictionary = ['Bob','Br','Btu','Bud','C','Ca','Cal','Cd','Cf','Che', 'Chi','Ci','Cid','Cl','Cm','Co','Col']
    #dictionary = ['bat', 'god', 'gid', 'dig', 'dog', 'mad']
    dictionary = ['cat', 'bat', 'bet', 'bed', 'at', 'ad', 'ed']
    graph = construct_graph(dictionary)
    """
    for g in graph.keys():
        print g, graph[g]
    """
    transform_word(graph, 'cat', 'bed')

if __name__ == "__main__":
    main()
