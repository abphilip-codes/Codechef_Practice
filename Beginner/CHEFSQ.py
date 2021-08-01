# https://www.codechef.com/problems/CHEFSQ

for T in range(int(input())):
    N=int(input())
    n=list(map(int,input().split()))
    M=int(input())
    m=list(map(int,input().split()))
    for i in m:
        if(i not in n): 
            print("No")
            break
    else: print("Yes")