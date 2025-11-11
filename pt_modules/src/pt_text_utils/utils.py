# utils.py


# some text utilities


import pyfiglet


def pt_word_count(text):
    words = text.split()
    return len(words)

def intro():
    f = pyfiglet.figlet_format("A SICCU", font='slant')
    print(f)
