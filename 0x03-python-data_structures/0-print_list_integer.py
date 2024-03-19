#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """My function
    Args:
        my_list: list void
    Returns:
        The return none value
    """
    for i in my_list:
        if type(i) == int:
            print('{}'.format(i))
