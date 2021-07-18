# https://www.codechef.com/problems/REMISS

for T in range(int(input())): 
    l = list(map(int,input().split()))
    print(max(l),sum(l))