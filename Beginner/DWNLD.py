# https://www.codechef.com/problems/DWNLD

for TC in range(int(input())):
    n,k=map(int,input().split())
    T,s=[],0
    for i in range(n):
        t,d=map(int,input().split())
        T.append(t)
        if(sum(T)>k): s,k=s+((sum(T)-k)*d),sum(T)
    print(s)