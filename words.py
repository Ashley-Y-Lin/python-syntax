words = ["hello", "Elephant", "hey", "goodbye", "yo", "yes", "elie"]


def print_upper_words(words):
    """turn an array of words to uppercase, and print each word on a
    separate line"""

    for word in words:
        print(word.upper())


def print_upper_words_e(words):
    for word in words:
        if word.lower().startswith("e"):
            print(word.upper())


def print_upper_words_filtered(words, starts_with={}):
    for word in words:
        if word.lower()[0] in starts_with:
            print(word.upper())
