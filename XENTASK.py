# https://www.codechef.com/problems/XENTASK

for T in range(int(input())):
    n,x,y,s1,s2=int(input()),list(map(int,input().split())),list(map(int,input().split())),0,0
    for z in range(0,n,2): s1,s2=s1+x[z],s2+y[z]
    for z in range(1,n,2): s1,s2=s1+y[z],s2+x[z]
    print(min(s1,s2))