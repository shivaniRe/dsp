#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import sys
import random

try:
    f = sys.argv[1]
    wcount = sys.argv[2]
except:
    print "Enter two arguments"

words = []
words_dict = {}
wcount = 40
fopen = open(f, 'r')
for word in fopen.read().split(' '):
    words.append(word)

words_list = []
w1 = words[0]
w2 = words[1]
for word in words[2:]:
    words_list.append([w1,w2,word])
    w1, w2 = w2, word

# generate output
start_list = random.choice(words_list)
w1, w2 = start_list[0], start_list[1]

output_words = []

while len(output_words) <= wcount:
    sample_list = []
    for l in words_list:
        if w1 == l[0] and w2 == l[1]:
            sample_list.append(l)
    next_list = random.choice(sample_list)
    output_words.append(next_list[2])
    w1, w2 = next_list[1], next_list[2]
    
print ' '.join(w for w in output_words)


