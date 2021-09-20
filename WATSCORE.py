# https://www.codechef.com/problems/WATSCORE

for T in range(int(input())):
    n,ans=int(input()),[0]*11
    for i in range(n):
        P,S=map(int,input().split())
        if(ans[P-1]<S): ans[P-1]=S
    print(sum(ans[0:8]))