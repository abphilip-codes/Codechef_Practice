# https://www.codechef.com/problems/PSGRADE

for _ in range(int(input())):
    l=list(map(int,input().split()))
    print("YES") if(l[0]<=l[4] and l[1]<=l[5] and l[2]<=l[6] and l[3]<=sum(l[4:8])) else print("NO")