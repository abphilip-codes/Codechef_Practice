# https://www.codechef.com/problems/TRICOIN

for T in range(int(input())):
    n,s=int(input()),1
    while((s*(s+1))/2<=n): s+=1
    print(s-1)