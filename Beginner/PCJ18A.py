# https://www.codechef.com/problems/PCJ18A

for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    print("YES") if(max(a)>=x) else print("NO")