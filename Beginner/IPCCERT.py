# https://www.codechef.com/problems/IPCCERT

n,m,k=map(int,input().split())
ans=0
for _ in range(n):
    t=list(map(int,input().split()))
    if(sum(t[:-1])>=m and t[-1]<=10): ans+=1
print(ans)