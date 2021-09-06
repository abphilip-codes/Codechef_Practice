# https://www.codechef.com/problems/HMAPPY2

for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    for z in range(1,n+1):
        if(z%a==0 or z%b==0): 
            if not (z%a==0 and z%b==0): k-=1
    print("Lose") if(k) else print("Win")