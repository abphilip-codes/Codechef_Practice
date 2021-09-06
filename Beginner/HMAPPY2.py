# https://www.codechef.com/problems/HMAPPY2

for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    x,y=a,b
    while(y): x,y=y,x%y
    print("Lose") if(k>(n//a+n//b-2*(n//((a*b)//x)))) else print("Win")