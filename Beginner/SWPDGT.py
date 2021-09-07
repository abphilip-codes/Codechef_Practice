# https://www.codechef.com/problems/SWPDGT

for _ in range(int(input())):
    a,b=map(int,input().split())
    a1,a2,b1,b2,m=a%10,a//10,b%10,b//10,0
    if(a2): m=max(m,a2*10+b2+a1*10+b1)
    if(b2): m=max(m,b1*10+a1+b2*10+a2)
    print(m)