# https://www.codechef.com/problems/BRLADDER

for T in range(int(input())):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    print("YES") if((a%2!=0 and (b-a)<=2) or (a%2==0 and (b-a)==2)) else print("NO")