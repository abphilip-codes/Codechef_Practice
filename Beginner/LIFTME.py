# https://www.codechef.com/problems/LIFTME

for T in range(int(input())):
    n,q=map(int,input().split())
    ans=c=0
    for z in range(q):
        f,d=map(int,input().split())
        ans,c=ans+abs(c-f)+abs(f-d),d
    print(ans)