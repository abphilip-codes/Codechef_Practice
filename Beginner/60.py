# https://www.codechef.com/problems/FRGTNLNG

for T in range(int(input())):
    N,K=map(int,input().split())
    n,k=list(input().split()),[]
    for j in range(K): k.append(list(input().split()))
    for i in n:
        mark="NO"
        for j in range(K): 
            if(i in k[j]): mark="YES"
        print(mark,end=" ")
    print()