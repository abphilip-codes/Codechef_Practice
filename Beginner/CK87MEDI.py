# https://www.codechef.com/problems/CK87MEDI

for T in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    print(l[(n+k-1)//2])