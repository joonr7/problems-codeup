#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# Problem link: https://codeup.kr/problem.php?id=4701
'''input
5
-2 4 -99 -1 98
'''

'''output
-99 98
'''
import time
def input_reader():
    solution_num = int(input())
    solution_list = list(map(int, input().split(" ")))

    # Error 
    assert solution_num == len(solution_list), "Input num is different from the length of input list"
    assert (len(solution_list)>=2), "There should be at least two solutions."

    # Sort
    solution_list.sort()

    # devide into acid and alkali
    list_acid = []
    list_alkali = []
    for solution in solution_list:
        if solution > 0:
            list_acid.append(solution)
        else:
            list_alkali.append(solution)

    list_alkali.reverse()
    return list_acid, list_alkali

def makeAbsOrderList(list_a, list_b):
    abs_arr_list = []

    if len(list_a) == 0:
        return list_b
    if len(list_b) == 0:
        return list_a

    a,b = list_a.pop(0),list_b.pop(0)
    while(True):
        if abs(a) < abs(b):
            abs_arr_list.append(a)
            try:
                a = list_a.pop(0)
            except:
                abs_arr_list.append(b)
                for b in list_b:
                    abs_arr_list.append(b)
                break    
        else:
            abs_arr_list.append(b)
            try:
                b = list_b.pop(0)
            except:
                abs_arr_list.append(a)
                for a in list_a:
                    abs_arr_list.append(a)
                break
    return abs_arr_list

def findBestPair(abs_arr_list):
    min_sum = 2000000000
    for i in range(len(abs_arr_list)-1):
        if abs(abs_arr_list[i] + abs_arr_list[i+1]) < min_sum:
            min_sum = abs(abs_arr_list[i] + abs_arr_list[i+1])
            best_pair = [abs_arr_list[i], abs_arr_list[i+1]]
    best_pair.sort()
    return best_pair

def main(): 
    sorted_acid_list, sorted_alkali_list = input_reader()
    abs_arr_list = makeAbsOrderList(sorted_acid_list, sorted_alkali_list)
    best_pair = findBestPair(abs_arr_list)
    print(best_pair[0], best_pair[1])

if __name__ == "__main__":
    main()


