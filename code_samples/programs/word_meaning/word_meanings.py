# This program provides meanings of a word if available. If the meaning not available it will suggest the closest word.
# User then can request for suggested word meaning. If there are no suggestions available or the user select incorrect
# index of suggested word then it will just exit.
# It reads a json file which contains a mapping from a word -> list of meanings
# Words suggested in case of mismatch are max 4 and with a match score of 0.7


import json  # This is to load the json file in a dictionary format in one of the variable
from difflib import \
    get_close_matches  # this is to do a sequence match and get the closest matching string to random input

meaning_dict = json.load(open("word_meanings_data.json"))


def find_meaning(word):
    word_meaning = None
    if word in meaning_dict:
        word_meaning = meaning_dict[word]
    elif word.title() in meaning_dict:
        word_meaning = meaning_dict[word.title()]
    elif word.lower() in meaning_dict:
        word_meaning = meaning_dict[word.lower()]
    elif word.upper() in meaning_dict:
        word_meaning = meaning_dict[word.upper()]
    return word_meaning


def print_list_values(values):
    for i, meaning in zip(range(len(values)), values):
        print("%d. %s" % (i + 1, meaning))


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def handle_suggested_words(suggested_words):
    option = input("Select the word # : ")
    # Ternary if else - condition_if_true if condition else condition_if_false
    int_option = int(option) if is_int(option) else 0
    if is_int(option) and int_option in range(1, 5):
        print_list_values(find_meaning(suggested_words[int_option - 1]))
    else:
        print("Invalid Option")


def handle_meanings_not_found():
    suggested_words = get_close_matches(input_word, meaning_dict.keys(), 4, 0.7)
    if suggested_words is not None and len(suggested_words) > 0:
        print("Did you mean ?:")
        print_list_values(suggested_words)
        handle_suggested_words(suggested_words)
    else:
        print("Meaning Not Found - the word may not be spelled correct or does not exist")


input_word = input("Enter a word: ").lstrip()
meanings = find_meaning(input_word)
if meanings is not None:
    print_list_values(meanings)
else:
    handle_meanings_not_found()
