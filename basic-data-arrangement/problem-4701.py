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
def input_reader():
    solution_num = int(input())
    solution_list = list(map(int, input().split(" ")))

    # Error 
    assert solution_num == len(solution_list), "Input num is different from the length of input list"
    assert (len(solution_list)>=2), "There should be at least two solutions."

    # Sort
    solution_list.sort()

    return solution_num, solution_list

def findBestPair(num, sorted_list):
    index_l = 0
    index_r = num - 1

    best_il = index_l
    best_ir = index_r

    min_sum = sorted_list[best_il] + sorted_list[best_ir]

    while index_l < index_r:
        temp_sum = sorted_list[index_l] + sorted_list[index_r]
        if abs(temp_sum) < abs(min_sum):
            min_sum = temp_sum
            best_il = index_l
            best_ir = index_r
            if temp_sum == 0:
                break
        if temp_sum < 0:
            index_l += 1
        else: 
            index_r -= 1

    return [sorted_list[best_il], sorted_list[best_ir]]

def main(): 
    solution_num, sorted_solution_list = input_reader()
    best_pair = findBestPair(solution_num, sorted_solution_list)
    print(best_pair[0], best_pair[1])

if __name__ == "__main__":
    main()


