# https://www.codechef.com/problems/ALTARAY

for T in range(int(input())):
    n,l,c,s=int(input()),list(map(int,input().split())),1,""
    for i in range(n-1,0,-1):
        if(l[i]^l[i-1]<0): s,c=s+str(c)+" ",c+1
        else: s,c=s+str(c)+" ",1
    s+=str(c)
    print(s[::-1])