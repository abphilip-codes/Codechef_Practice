# https://www.codechef.com/problems/SEDARR

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(0) if(sum(a)%k==0) else print(1)