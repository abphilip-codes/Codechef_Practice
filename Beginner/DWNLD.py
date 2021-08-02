# https://www.codechef.com/problems/DWNLD

for TC in range(int(input())):
    n,k=map(int,input().split())
    T=s=i=0
    while(True):
        t,d=map(int,input().split())
        if(T+t>k):break
        T,i=T+t,i+1
    s+=((T+t-k)*d)
    for j in range(i+1,n):
        t,d=map(int,input().split())
        s+=(t*d)
    print(s)