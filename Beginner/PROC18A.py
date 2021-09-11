# https://www.codechef.com/problems/PROC18A

for _ in range(int(input())):
    n,k=map(int,input().split())
    a,m=list(map(int,input().split())),0
    for z in range(n-k+1): m=max(m,sum(a[z:z+k]))
    print(m)