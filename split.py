# Takes a file of words and split it into seperate files based on the length of the word

import sys

with open('files/english3.txt', 'r') as f:
    dictionary = f.read()
    f.close()

dictionary = [x.lower() for x in dictionary.split('\n')]
i = 0
for x in dictionary:
    lengthOfWord = len(x)
    theFileName = "files/" + str(lengthOfWord) + "words.txt"
    with open(theFileName, 'a+') as g:
        g.write(x + "\r")
        g.close()