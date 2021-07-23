# https://www.codechef.com/problems/COMM3

for T in range(int(input())):
    n=int(input())
    for i in range(3):
        l,k=list(map(int,input().split())),"yes"
        if(n<sum(l)): k="no"
    print(k)