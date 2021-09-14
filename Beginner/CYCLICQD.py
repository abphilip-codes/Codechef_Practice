# https://www.codechef.com/problems/CYCLICQD

for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    print("YES") if(a+c==180 and b+d==180) else print("NO")