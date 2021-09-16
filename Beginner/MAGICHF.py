# https://www.codechef.com/problems/MAGICHF

for _ in range(int(input())):
    n,x,s=map(int,input().split())
    for z in range(s):
        a,b=map(int,input().split())
        if(a==x): x=b 
        elif(b==x): x=a
    print(x)