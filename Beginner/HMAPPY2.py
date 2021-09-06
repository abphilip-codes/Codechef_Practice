# https://www.codechef.com/problems/HMAPPY2

def gcd(x,y):
   while(y): x,y=y,x%y
   return x
for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    lcm=a*b/gcd(a,b)
    print("Lose") if(k>(n//a+n//b-2*(n//int(lcm)))) else print("Win")