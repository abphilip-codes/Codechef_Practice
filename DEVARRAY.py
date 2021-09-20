# https://www.codechef.com/problems/DEVARRAY

n,Q=map(int,input().split())
max1,min1,a=-99999999999,99999999999,list(map(int,input().split()))
for z in range(n): min1,max1 = min(min1,a[z]),max(max1,a[z])
for z in range(Q): print("Yes") if(int(input()) in range(min1,max1+1)) else print("No")