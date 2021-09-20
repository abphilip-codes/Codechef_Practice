# https://www.codechef.com/problems/CHNGOR

for _ in range(int(input())):
    n,a,ans=int(input()),list(map(int,input().split())),0
    for z in a: ans=ans|z
    print(ans)