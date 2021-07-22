# https://www.codechef.com/problems/FRUITS

for T in range(int(input())):
    n,m,k = map(int,input().split())
    print(max(abs(n-m)-k,0))