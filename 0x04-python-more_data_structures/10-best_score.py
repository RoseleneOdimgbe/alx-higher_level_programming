#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    my_list = a_dictionary.values()

    max_value = max(my_list)
    for key, val in a dictionary.items():
        if val == max_value:
            return key
