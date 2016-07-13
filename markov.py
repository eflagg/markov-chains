from random import choice
import sys


def open_and_read_file():
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.

    """

    file_path = sys.argv[1]
    input_file = open(file_path).read()
    return input_file

    # your code goes here

    #return "This should be a variable that contains your file text as one long string"


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    #print words
    
    for i in range(len(words) - n):
        # next_word = words[i+2]
        #print "Next Word",next_word
        key_word_tuple = tuple(words[i:(i + n)])
        # print key_word_tuple
        #, words[i + 1])
        chains[key_word_tuple] = chains.get(key_word_tuple, [])
        # if (i + 2) < len(words):
        next_word = words[i+n]
        chains[key_word_tuple].append(next_word)
        
        
    #print chains
    return chains


def make_text(chains, n):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    random_key = choice(chains.keys())
    text = " ".join(random_key)
    #random_key[0] + " " + random_key[1]
    #Loops through dictionary called chains and raondomly 
    #chooses a next word and adds it to string
    while True:

        random_add = choice(chains[random_key])
        print random_key[1-n:]
        print random_add
        new_list=list(random_key[1-n:])
        new_list.append(random_add)
        random_key = tuple(new_list)
        #random_key = tuple([random_key[1-n:], random_add])
        #test_key = random_key[n+1:]
        print "test random key: ", random_key, "random add: ", random_add
        sequence = (text,random_add)
        text = " ".join([text, random_add])
        #text = text + " " + random_add
        # if the key has no value, stop, you're at the end!
        if random_key not in chains:
            break

    return text


#input_path = "green-eggs.txt"

#input_path = "gettysburg.txt"

input_text = open_and_read_file()

chains = make_chains(input_text, 3)

random_text = make_text(chains, 3)

print random_text
