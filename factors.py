#!/usr/bin/python3
def factors(my_list):
    """check factor of number in a list"""
    import sys

    if len(my_list) == 0 or my_list is None:
        print("An error occured")
    for q in my_list:
       i = int(q)
       for j in range(2, sys.maxsize):
           if i % j == 0:
               print("{:d}={:d}*{:d}".format(i, int(i/j), j))
               break

def factorize():
    """factor two numbers"""
    import sys

    fact = sys.argv
    if len(fact) < 2:
        print("Error!:<USAGE> ./factors file")
        exit(98)
    f_name = ''
    if len(fact) == 2:
        f_name = fact[1]
    if len(fact) == 3:
        f_name = fact[2]
    with open(f_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    factors(lines)
factorize()
