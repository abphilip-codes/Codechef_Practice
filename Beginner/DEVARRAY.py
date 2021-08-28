# https://www.codechef.com/problems/DEVARRAY

n,Q=map(int,input().split())
a=list(map(int,input().split()))
for z in range(Q): print("Yes") if(int(input()) in range(min(a),max(a)+1)) else print("No")