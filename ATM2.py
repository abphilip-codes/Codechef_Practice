# https://www.codechef.com/problems/ATM2

for T in range(int(input())):
    ret=""
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        if(a[i]<=k):
            ret+="1"
            k-=a[i]
        else: ret+="0"
    print(ret)