from time import strftime
import re


def sorting(lst):
    lst.sort(key=len)
    return lst

def anagram_check(word,check):
    for letter in word:
        if letter in check:
            check = check.replace(letter, '', 1)
        else:
            return 0
    return 1

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(type, phrase):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write('{}, {}, {} \n'.format(timestamp, type, phrase))
    data.close()

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


def missing_letter(text):
    wordInput = str(text)
    wordLength = len(wordInput)
    fileToUse = "files/" + str(wordLength) + "words.txt"
    with open(fileToUse, 'r') as f:
        dictionary = f.read()
        f.close
    searchString = wordInput.replace("*", "[\w\.-]")
    theAnswers = re.findall(searchString, dictionary)   
    return theAnswers

def anagram_s(text):
    scrambled = str(text)
    scrambledLength = len(scrambled)
    results=[]
    f=open("files/english3.txt", "r")
    for x in f:
        x=x.strip()
        if len(x) == scrambledLength:
            if anagram_check(x,scrambled):
                print(x)
                results.append(x)
    f.close()
    return sorting(results)


def words_in_word(text):
    scrambled = str(text)
    scrambledLength = len(scrambled)
    results=[]
    f=open("files/english3.txt", "r")
    for x in f:
        x=x.strip()
        if len(x) <= scrambledLength and len(x) > 1:
            if anagram_check(x,scrambled):
                print(x)
                results.append(x)
    f.close()
    return sorting(results)
