#!/usr/bin/python3
def is_sqrd(num):
    """check if a number is squared"""
    import math

    a = int(math.sqrt(num))
    if (a * a == num):
        return (True)
    return (False)

def is_RSA(n):
    """Get RSA of a number"""
    import math
    from prime import is_prime

    a = int(math.sqrt(n)) + 1
    while True:
        b = a ** 2 - n
        if is_sqrd(b):
            c = math.sqrt(b)
            break
        a = a + 1
    print("{:d}={:d}*{:d}".format(int(n), int(a + c), int(a - c)))

def start():
    """File entry."""
    import sys

    fact = sys.argv
    if len(fact) < 2:
        print("Error!: <USAGE> -> ./rsa file")
        exit(98)
    f_name = ''
    if len(fact) == 2:
        f_name = fact[1]
    if len(fact) == 3:
        f_name = fact[2]
    with open(f_name ) as file_in:
        lines = []
        for line in file_in:
            lines.append(line);
    if len(lines) == 0:
        print("The file is empty")
        exit(98)
    is_rsa(int(lines[0]))
start()
