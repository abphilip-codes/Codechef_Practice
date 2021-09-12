# https://www.codechef.com/submit/CHEFDETE

n,l=int(input()),list(map(int,input().split()))
a=[0]*(n+1)
for z in range(n): a[l[z]]=1
for z in range(1,n+1): 
    if(a[z]==0): print(z,end=" ")     
print()