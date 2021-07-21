# https://www.codechef.com/problems/SMPAIR

for T in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(sum(sorted(l)[:2]))