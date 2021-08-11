# https://www.codechef.com/problems/OMWG

for T in range(int(input())):
    n,m=map(int,input().split())
    print(n*(m-1)+m*(n-1))