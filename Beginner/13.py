# https://www.codechef.com/problems/TLG

p1=p2=al=0
ans=""
for T in range(int(input())): 
    a,b = map(int,input().split(" "))
    p1,p2 = p1+a,p2+b
    if(abs(p1-p2)>=al):
        al=abs(p1-p2)
        if(p1>p2): ans="1 {}".format(p1-p2)
        else: ans="2 {}".format(p2-p1)
print(ans)