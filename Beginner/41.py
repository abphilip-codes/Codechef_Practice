# https://www.codechef.com/problems/GDOG

for T in range(int(input())):
    n,k = map(int,input().split())
    l = [0]
    for z in range(1,k+1): l.append(n%z)
    print(max(l))