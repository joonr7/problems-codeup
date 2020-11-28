#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# Problem link: https://codeup.kr/problem.php?id=1085

"""
# Input Example (h b c s)
44100 16 2 10
"""

"""
# Output Example
1.7 MB
"""


def bit2MB(input_bit):
    M = 1024*1024
    BYTE = 8
    output_mb = round(input_bit / (M*BYTE), 1)
    return output_mb

def calculateSize(hertz, bit, channel, seconds):
    return hertz * bit * channel * seconds

def main():
    hertz, bit, channel, seconds = map(int, input().split(" "))
    size_bit = calculateSize(hertz, bit, channel, seconds)
    size_mb = bit2MB(size_bit)
    print(f"{size_mb} MB")

if __name__ == "__main__":
    main()
