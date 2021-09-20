# https://www.codechef.com/problems/POPGATES

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(input().split())
    for z in range(n-1,n-k-1,-1):
        if(l[z]=='H'):
            for y in range(z): 
                if(l[y]=='H'): l[y]='T'
                else: l[y]='H'
    print(l[:n-k].count('H'))