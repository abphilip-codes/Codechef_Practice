# https://www.codechef.com/problems/CHEFRUN

for T in range(int(input())):
    x1,x2,x3,v1,v2=map(int,input().split())
    d1,d2=abs(x1-x3),abs(x2-x3)
    if(d1/v1>d2/v2): print("Kefa")
    elif(d1/v1<d2/v2): print("Chef")
    else: print("Draw")