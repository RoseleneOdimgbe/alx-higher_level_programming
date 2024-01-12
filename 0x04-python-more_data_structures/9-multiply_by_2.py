#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_d = {}
    for key, values in a_dictionary.items():
        new_d[key] = values * 2
    return new_d
