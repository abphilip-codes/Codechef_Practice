# https://www.codechef.com/problems/SWPDGT

for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=a+b
    if(a>=10): ans=max(ans,a//10+a%10+(b%10+b//10)*10)
    if(b>=10): ans=max(ans,b//10+b%10+(a%10+a//10)*10)
    print(ans)