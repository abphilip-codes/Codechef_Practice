# https://www.codechef.com/problems/CV 

for T in range(int(input())):
    n,s,v,ans=int(input()),input(),['a','e','i','o','u'],0
    for i in range(n-1):
        if(s[i] not in v and s[i+1] in v): ans+=1
    print(ans)