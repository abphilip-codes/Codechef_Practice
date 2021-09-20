# https://www.codechef.com/problems/CCISLAND

for _ in range(int(input())):
    l=list(map(int,input().split()))
    print("YES") if(l[2]*l[4]<=l[0] and l[3]*l[4]<=l[1]) else print("NO")