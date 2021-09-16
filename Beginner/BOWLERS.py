# https://www.codechef.com/problems/BOWLERS

for _ in range(int(input())):
    n,k,l=map(int,input().split())
    a=[z%k+1 for z in range(n)]
    for z in range(1,k+1):
        if(a.count(z)>l): 
            print(-1)
            break
    else: print(*a)