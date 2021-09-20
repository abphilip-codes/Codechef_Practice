# https://www.codechef.com/problems/PRICECON

for T in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    for i in a:
        s-=min(k,i)
    print(s)