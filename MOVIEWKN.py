# https://www.codechef.com/problems/MOVIEWKN

for T in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    pos,m,k=[],0,0
    for i in range(n):
        if(l[i]*r[i]>m): m,k,pos=l[i]*r[i],r[i],[i]
        elif(l[i]*r[i]==m): 
            if(r[i]>k): k,pos=r[i],[i]
            elif(r[i]==k): pos.append(i)
    print(min(pos)+1)