# https://www.codechef.com/problems/PRGIFT

for T in range(int(input())):
    n,k=map(int,input().split())
    a,c=list(map(int,input().split())),False
    for z in range(n):
        for y in range(z,n):
            if(k==len([1 for x in range(z,y+1) if(a[x]%2==0)])): c=True
    print("YES") if(c) else print("NO")