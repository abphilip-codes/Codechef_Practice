# https://www.codechef.com/problems/WATMELON

for T in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    print("YES") if(sum(l)>=0) else print("NO")