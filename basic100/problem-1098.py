#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
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


def main():
    # input parser
    grid_h, grid_w = map(int, input().split(" "))
    bar_number = int(input())
    list_bar_info = []
    for i in range(bar_number):
        bar_length, bar_direction, bar_x, bar_y = map(int, input().split(" "))
        list_bar_info.append({"length":bar_length, "direction": bar_direction, "x": bar_x, "y": bar_y})
    
    # initialize grid
    grid = []
    for i in range(grid_h):
        row = []
        for j in range(grid_w):
            row.append(0)
        grid.append(row)
    
    # put the bars on grid
    for bar in list_bar_info:
        for i in range(bar["length"]):
            bar_grid_x = bar["x"]-1 + i*bar["direction"]
            bar_grid_y = bar["y"]-1 + i*(1-bar["direction"])  
            grid[bar_grid_x][bar_grid_y] = 1

    # output
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # execute only if run as a script
    main()
