# https://www.codechef.com/problems/RECTANGL

for T in range(int(input())):
    l = list(map(int,input().split()))
    print("YES") if((l.count(sorted(l)[0]) and l.count(sorted(l)[-1]))==2) else print("NO")