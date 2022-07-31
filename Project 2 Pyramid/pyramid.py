'''
Sharon Steinke
CS 1410
Project 2: Pyramids
Input: number of rows
Output: pyramid with the weight that
that person in the pyramid is shouldering

I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project
if I am found in violation of this policy.
'''
import sys
import time

COUNT = 0
CACHE_COUNT = 0
cache = {}
def weight_on(row, column):
    """
    input: row and column
    row and column =  position in pyramid
    (0,0) = top of pyramid
    output: the weight that the peron in specified position is shouldering
    """
    global COUNT, CACHE_COUNT
    lbs = 200
    if (row, column) in cache:
        CACHE_COUNT += 1
        COUNT += 1
        return cache[(row, column)]
    if column == 0:
        if row == 0 and column == 0:
            COUNT += 1
            return 0
        value = lbs/2 + weight_on(row-1, column)/2
        cache[(row, column)] = value
        COUNT += 1
        return value
    if column == row:
        value = lbs/2 + weight_on(row-1, column-1)/2
        cache[(row, column)] = value
        COUNT += 1
        return value
    value = lbs/2 + weight_on(row-1, column)/2 + lbs/2 + weight_on(row-1, column-1)/2
    COUNT += 1
    cache[(row, column)] = value
    return value



def main():
    '''
    input: number of rows
    output: pyramid with specified rows
    '''

    rows = int(sys.argv[1])
    start_time = time.perf_counter()
    for row in range(rows):
        for column in range(row+1):
            print(f"{weight_on(row, column):.2f}", end = ' ')
        print()
    stop_time = time.perf_counter()
    print(f'Elapsed time: {stop_time-start_time} seconds')
    print(f'Number of function calls: {COUNT}')
    print(f'Number of cache hits: {CACHE_COUNT}')

if __name__ == "__main__":
    main()
