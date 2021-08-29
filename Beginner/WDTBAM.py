# https://www.codechef.com/problems/WDTBAM

for T in range(int(input())):
    n,q,a,w,s=int(input()),input(),input(),list(map(int,input().split())),0
    for z in range(n): 
        if(q[z]==a[z]): s+=1
    print(w[s])