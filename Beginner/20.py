# https://www.codechef.com/problems/FLOW013

for T in range(int(input())):
    l = list(map(int,input().split()))
    print("YES") if(sum(l)==180) else print("NO")