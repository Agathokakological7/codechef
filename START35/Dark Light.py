"""
Problem

Tonmoy has a special torch. The torch has 44 levels numbered 11 to 44 and 22 states (\texttt{On}On and \texttt{Off}Off). 
Levels 1, 2,1,2, and 33 correspond to the \texttt{On}On state while level 44 corresponds to the \texttt{Off}Off state.

The levels of the torch can be changed as:

Level 11 changes to level 22.
Level 22 changes to level 33.
Level 33 changes to level 44.
Level 44 changes to level 11.

Given the initial state as KK and the number of changes made in the levels as NN, find the final state of the torch. 
If the final state cannot be determined, print \texttt{Ambiguous}Ambiguous instead.

Input Format
First line will contain TT, the number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers N, KN,K - the number of changes made in the levels and initial state of the torch.
Here, K = 0K=0 denotes \texttt{Off}Off state while K = 1K=1 denotes \texttt{On}On state.

Output Format
For each test case, output in a single line, the final state of the torch, i.e. \texttt{On}On or \texttt{Off}Off.
If the final state cannot be determined, print \texttt{Ambiguous}Ambiguous instead.
You may print each character of the string in uppercase or lowercase (for example, the strings oN will all be treated as identical).

"""

# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    if(k==0):
        if(n%4==0):
            print("off")
        else:
            print("on")
    
    elif(k==1):
        
        if(n%4==0):
            print("on")
        else:
           print("ambiguous")

            
