# https://www.codechef.com/problems/RPD

for T in range(int(input())):
    n,s,ans=int(input()),list(map(int,input().split())),0
    for i in range(0,n):
        for j in range(i+1,n):
            p=s[i]*s[j]
            k=0
            while(p>0): k,p=k+p%10,p//10
            ans=max(ans,k)
    print(ans)