# https://www.codechef.com/problems/FBMT

for _ in range(int(input())):
    s=[]
    for n in range(int(input())): s.append(input())
    st=list(set(s))
    a,b=s.count(st[0]),s.count(st[1])
    if(a>b): print(st[0])
    elif(a<b): print(st[1])
    else: print("Draw")