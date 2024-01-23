#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """	This prints the first x elements of a list that are integers

    Args:
        my_list (list): this is the list to print elements from
        x (int): this is the number of elements to print

    Returns:
        the number of elements printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
