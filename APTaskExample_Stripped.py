from pprint import pprint
from colorama import Fore, init, Style

init()

def find_duplicates(words):
    ordered_set_words = {}

    for word in words:
        ordered_set_words[word] = ordered_set_words[word]+1 if word in ordered_set_words else 1
    
    return ordered_set_words

def highlight_dupes(words, ordered_set_words):

    for word in words:
        if ordered_set_words[word] > 1:
            print(Fore.RED + word, end=" ")
        else:
            print(Style.RESET_ALL + word, end=" ")

print("Highlight duplacate words in text")
text = input("Input a block of text: ")
words = text.split()
duplacates = find_duplicates(words)

highlight_dupes(words,duplacates)