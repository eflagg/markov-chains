from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    input_file = open(file_path).read()
    return input_file

    # your code goes here

    #return "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
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
    
    for i in range(len(words) - 1):
        # next_word = words[i+2]
        #print "Next Word",next_word
        key_word_tuple = (words[i], words[i + 1])
        chains[key_word_tuple] = chains.get(key_word_tuple, [])
        if (i + 2) < len(words):
            next_word = words[i+2]
            chains[key_word_tuple].append(next_word)
        
        
    #print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    random_key = choice(chains.keys())
    text = random_key[0] + " " + random_key[1]
    #Loops through dictionary called chains and raondomly 
    #chooses a next word and adds it to string
    while True:

        random_add = choice(chains[random_key])
        random_key = (random_key[1], random_add)
        text = text + " " + random_add
        # if the key has no value, stop, you're at the end!
        if chains[random_key] == []:
            break

    return text


input_path = "green-eggs.txt"

input_text = open_and_read_file(input_path)

chains = make_chains(input_text)

random_text = make_text(chains)

print random_text
