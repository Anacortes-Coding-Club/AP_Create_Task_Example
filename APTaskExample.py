from pprint import pprint
from colorama import Fore, init, Style

# Duplacate word highliter
# insert block of text
# record what words are the same

# initalize the colorama library
init()

# takes a list of words and returns a dictionary of words and how many times they are duplicated in the text
def find_duplicates(words):
    # construct empty dictionary
    ordered_set_words = {}

    # for each word in words add 1 each time it is in the list
    for word in words:
        ordered_set_words[word] = ordered_set_words[word]+1 if word in ordered_set_words else 1
    
    return ordered_set_words

# prints the original text and highlights the duplicate words
def highlight_dupes(words, ordered_set_words):

    for word in words:
        if ordered_set_words[word] > 1:
            # print in red text
            print(Fore.RED + word, end=" ")
        else:
            # print in default text
            print(Style.RESET_ALL + word, end=" ")

# program printout description
print("Highlight duplacate words in text")
text = input("Input a block of text: ")

# turn text string into a list of words
words = text.split()

# find the dups and print with color
highlight_dupes(words,find_duplicates(words))
