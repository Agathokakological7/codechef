"""
Problem

You have a grid with NN rows and MM columns. You have two types of tiles — one of dimensions 2 \times 22×2 and the other of dimensions 1 \times 11×1. You want to cover the grid using these two types of tiles in such a way that:

Each cell of the grid is covered by exactly one tile; and
The number of 1 \times 11×1 tiles used is minimized.
Find the minimum number of 1 \times 11×1 tiles you have to use to fill the grid.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line containing two space-separated integers N, MN,M.

Output Format
For each test case, print on a new line the minimum number of 1 \times 11×1 tiles needed to fill the grid.

Constraints

1≤T≤10^4
1≤N,M≤10^4

Input      output

4
1 1          1
4 5          4
6 8          0
3 2          2

Explanation:
Test case 1: There is only one square in the grid, and it must be filled with a single 1 \times 1×1 tile.

Test case 2: One way of tiling the grid using 1\times 1×1 tiles exactly 4 times.

Test case 3: One way of tiling the grid using no 1\times 1×1 tiles.

Test case 4: One way of tiling the grid using 1\times 1×1 tiles

"""

# cook your dish here
for t in range(int(input())):
    n,m=map(int,input().split())
    if(n%2==0 and m%2==0):print(0)
    elif(n%2!=0 and m%2!=0):print(m+n-1)
    elif(n%2!=0):print(n and m)
    else:print(n or m)
    
