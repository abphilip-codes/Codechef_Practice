# https://www.codechef.com/problems/WDTBAM

for T in range(int(input())):
    n,q,a,w,s=int(input()),input(),input(),list(map(int,input().split())),1
    for z in range(n): 
        if(q[z]==a[z]): s+=1
    print(max(w[:s]))

for T in range(int(input())):
    n,c,a,p,s=int(input()),input(),input(),list(map(int,input().split())),0
    for z in range(len(c)):
        if(a[z]==c[z]): s+=1
    if(s==n): print(p[n])
    else:
        ans=0
        for z in range(s):
            ans=max(ans,p[z])
        print(ans)