# https://www.codechef.com/problems/THREEPTS

for T in range(int(input())):
    x1, y1 = [int(z) for z in input().split()]
    x2, y2 = [int(z) for z in input().split()]
    x3, y3 = [int(z) for z in input().split()]
    s = "NO"
    if(x1>x3): x1, x3 = x3, x1
    if(y1>y3): y1, y3 = y3, y1
    if(x1==x3):
        if(x1==x2 and y1<y2<y3): s = "YES"
    elif(y1==y3):
        if(y1==y2 and x1<x2<x3): s = "YES"
    else:
        if(x1<=x2<=x3 and y1<=y2<=y3 and (x1==x2 or x2==x3 or y1==y2 or y2==y3)): s = "YES"
    print(s)