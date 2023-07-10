#!/usr/bin/env python3

def print_fibonacci(length):
    s = []
    if length == 0:
        print([])
    elif length == 1:
        s.append(0)
        print(s)
    elif length == 2:
        s.append(0)
        s.append(1)
        print(s)
    elif length > 2:
        # s.append(s[0]+s[1])
        s.append(0)
        s.append(1)
        for x in range(1, length-1):
            s.append(s[-1]+s[-2])
            
        print(s)
            
    pass