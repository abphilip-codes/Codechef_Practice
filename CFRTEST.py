# https://www.codechef.com/problems/CFRTEST

for T in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(len(set(l)))