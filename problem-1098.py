#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# Problem link: https://codeup.kr/problem.php?id=1098

"""
# Input Example
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5
"""

"""
# Output Example
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
"""

def input_parser():
    grid_h, grid_w = map(int, input().split(" "))

    bar_number = int(input())
    list_bars = []
    for i in range(bar_number):
        bar_length, bar_direction, bar_x, bar_y = map(int, input().split(" "))
        list_bars.append({"length":bar_length, "direction": bar_direction, "x": bar_x, "y": bar_y})

    return grid_w, grid_h, list_bars

def init_grid(grid_w, grid_h):
    ret = []
    for i in range(grid_h):
        row = []
        for j in range(grid_w):
            row.append(0)
        ret.append(row)
    return ret

def put_bars(grid, list_bars):
    # bar: {'length': len, 'direction': dir, 'x': x, 'y': y}
    offset = 1
    for bar in list_bars:
        for i in range(bar["length"]):
            bar_grid_x = bar["x"]-offset + i*bar["direction"] 
            bar_grid_y = bar["y"]-offset + i*(1-bar["direction"])  
            grid[bar_grid_x][bar_grid_y] = 1
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def main():
    grid_w, grid_h, list_bars = input_parser()
    grid = init_grid(grid_w, grid_h)
    grid = put_bars(grid, list_bars)    
    print_grid(grid) 

if __name__ == "__main__":
    main()
