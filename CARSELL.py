# https://www.codechef.com/problems/CARSELL

for _ in range(int(input())):
    n,p,s=int(input()),sorted(list(map(int,input().split()))),0
    for z in range(n): s+=(max(p[n-z-1]-z,0)%1000000007)
    print(s%1000000007)