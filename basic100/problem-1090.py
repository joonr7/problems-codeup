#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# Problem link: https://codeup.kr/problem.php?id=1090

"""
# Input Example
2 3 7
"""

"""
# Output Example
1458
"""

def input_parser():
    a, r, n = map(int, input().split(" "))
    return a,r,n

def calculateGeometricSequence(a,r,n):
    ret = a
    for i in range(n-1):
        ret *= r
    return ret

def main():
    a,r,n = input_parser()
    print(calculateGeometricSequence(a,r,n))

if __name__ == "__main__":
    main()
