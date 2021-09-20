# https://www.codechef.com/problems/FFL

for T in range(int(input())):
    n,s=map(int,input().split())
    p,i,l=list(map(int,input().split())),list(map(int,input().split())),[]
    for z in range(n): l.append([i[z],p[z]])
    l.sort()
    c=0
    for z in range(n):
        if(l[z][0]==0 and c==0): s,c=s+l[z][1],c+1
        if(l[z][0]==1 and c==1): s,c=s+l[z][1],c+1
    print("yes") if(s<=100 and c==2) else print("no")