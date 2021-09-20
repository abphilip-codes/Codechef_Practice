# https://www.codechef.com/problems/CHNGIT

for T in range(int(input())):
    n,a=int(input()),list(map(int,input().split()))
    m=max(set(a),key=a.count)
    print(n-a.count(m))