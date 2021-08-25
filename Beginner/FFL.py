# https://www.codechef.com/problems/FFL

for T in range(int(input())):
    n,s=map(int,input().split())
    p,i,l=list(map(int,input().split())),list(map(int,input().split())),[]
    for z in range(n): l.append([i[z],p[z]])
    l.sort()
    s+=l[0][1]
    for z in range(n):
        if(l[z][0]==1):
            s+=l[z][1]
            break
    print("yes") if(s<=100) else print("no")