# https://www.codechef.com/problems/CHN15A

for T in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for a in l:
        if((a+k)%7==0): n+=1 
    print(n-len(l))