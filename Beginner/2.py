# https://www.codechef.com/problems/INTEST

n,k = map(int,input().split(' '))
ans=0
for i in range(n):
	if(int(input())%k)==0: ans+=1
print(ans)	