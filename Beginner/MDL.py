# https://www.codechef.com/problems/MDL

for T in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    m1,m2=max(l),min(l)
    m3,m4=l.index(m1),l.index(m2)
    print(m1,m2) if(m3<m4) else print(m2,m1)