#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# Problem link: https://codeup.kr/problem.php?id=1079

"""
# Input Example
x b k d l q g a c

"""

"""
# Output Example
x
b
k
d
l
q
"""

def input_parser():
    return 

def calculateGeometricSequence(a,r,n):
    ret = a
    for i in range(n-1):
        ret *= r
    return ret

def main():
    list_input = input().split(" ")
    for value in list_input:
        if value == 'q':
            print(value)
            break
        else:
            print(value)
    
if __name__ == "__main__":
    main()
