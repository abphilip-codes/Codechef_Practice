# https://www.codechef.com/problems/WDTBAM

for T in range(int(input())):
    n,c,a,p,s=int(input()),input(),input(),list(map(int,input().split())),0
    for z in range(len(c)):
        if(a[z]==c[z]): s+=1
    if(s==n): print(p[n])
    else: print(max(p[:s+1]))