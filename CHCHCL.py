# https://www.codechef.com/problems/CHCHCL

for T in range(int(input())):
    n,m=map(int,input().split())
    print("Yes") if(n*m%2==0) else print("No")