# https://www.codechef.com/problems/POPGATES

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for z in range(n-1,n-k-1,-1):
        if(l[z]=='H'):
            for y in range(z): l[y]='T' if(l[y]=='H') else l[y]='H'
                # if(l[y]=='H'): l[y]='T'
                # else: l[y]=
    print(l)