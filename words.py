def print_upper_words(words):
    """separates a list of words into their uppercase versions"""
    for word in words:
        print(word.upper())

def print_upper_words_restricted(words, letters):
    """doesn't work. print_upper_words() takes 1 positional argument but 2 were given. I don't understand this. """
    for word in words:
        if word[0] in letters:
           print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])