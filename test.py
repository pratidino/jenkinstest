#!/bin/env python3

def add(a,b):
        try:
                c = a+b
        except TypeError:
                c = str(a)+str(b)
        return c

if __name__ == "__main__":
        print ("Hello")
        s=10000+10000
        print (s)
        print(add(2000,2000))
        print(add('abc','def'))
