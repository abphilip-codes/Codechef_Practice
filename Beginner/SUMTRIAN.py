# https://www.codechef.com/problems/SUMTRIAN

for T in range(int(input())):
    n=int(input())
    a=[0]*n
    for z in range(n): a[z]=list(map(int,input().split()))
    for x in range(n-2,-1,-1):
        for y in range(0,x+1): a[x][y]+=max(a[x+1][y],a[x+1][y+1])
    print(a[0][0])