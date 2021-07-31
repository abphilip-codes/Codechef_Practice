# https://www.codechef.com/submit/RRJOKE

for T in range(int(input())):
    l,ans=[],0
    for n in range(int(input())): 
        l.append(list(map(int,input().split())))
        ans=ans^(n+1)
    print(ans)