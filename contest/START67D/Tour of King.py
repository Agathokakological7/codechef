"""
Problem

King loves to go on tours with his friends.

King has NN cars that can seat 55 people each and MM cars that can seat 77 people each. Determine the maximum number of people that can travel together in these cars.

Input Format
The first line of input contains a single integer TT, the number of test cases.
The first and only line of each test case contains two space-separated integers NN and MM — the number of 55-seaters and 77-seaters, respectively.
Output Format
For each test case, output on a new line the maximum number of people that can travel together.

Constraints :
 1≤T≤100
 0≤N,M≤100

Sample 1:

Input           output        
4                     
4 8              76          
2 13             101                  
14 5             105
8 8              96


"""


# cook your dish here
for t in range(int(input())):
    n,m=map(int,input().split())
    print((5*n)+(7*m))
