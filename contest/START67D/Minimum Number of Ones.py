"""
Your teacher gave you an assignment — given an integer NN, construct a binary string
for every i from 1 to N−1.

What is the minimum number of 1's such a binary string can contain?

Note: A binary string is a string consisting of only the digits 0 and 1.

Input Format:

The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case contains a single integer NN — the length of binary string you'd like to construct.

Output Format:
For each test case, output on a new line the minimum number of 11's required to complete the assignment.

Constraints:
1≤T≤1000
2≤N≤1000

Sample 1:

Input       Output
 6
 6            3                        
 8            4
 2            1
 3            1
 5            2
100           50

"""

# cook your dish here
for t in range(int(input())):
    n=int(input())
    print(n//2)

   
