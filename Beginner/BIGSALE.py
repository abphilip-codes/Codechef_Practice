# https://www.codechef.com/problems/BIGSALE

for _ in range(int(input())):
    ans=0.0
    for n in range(int(input())):
        p,q,d=map(int,input().split())
        ans+=((p*q)-(p*(((100+d)/100)*((100-d)/100))*q))
    print(ans)