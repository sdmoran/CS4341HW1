import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    contents = open(str(fname), 'r')

    # Create regexp for character filtering
    regex = re.compile('[^a-zA-Z ]')

    words = set([])

    for line in contents:
        for word in regex.sub(' ', line).split(): # Applies regex to line and splits into individual words
            words.add(word.lower()) # Converts word to lowercase and adds to set

    return words

def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    w1 = wordset(fname1) # Gets wordset corresponding to 1st text
    w2 = wordset(fname2) # Gets wordset corresponding to 2nd text

    return len(w1.intersection(w2)) / len(w1.union(w2))


