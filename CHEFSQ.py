# https://www.codechef.com/problems/CHEFSQ

for T in range(int(input())):
    N,n,M,m,s=int(input()),list(map(int,input().split())),int(input()),list(map(int,input().split())),0
    for i in range(M):
        if(m[i] not in n or n.index(m[i])<s): 
            print("No")
            break
        s=n.index(m[i])
    else: print("Yes")