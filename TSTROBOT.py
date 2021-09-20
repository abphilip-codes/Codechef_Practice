# https://www.codechef.com/problems/TSTROBOT

for _ in range(int(input())):
    n,x=map(int,input().split())
    s,ans=input(),[]
    ans.append(x)
    for z in range(n):
        if(s[z]=='L'): x-=1
        else: x+=1
        ans.append(x)
    print(len(set(ans)))