# https://www.codechef.com/problems/FLOW009

for T in range(int(input())):
    q,p = map(int,input().split())
    print("{:.6f}".format(q*p)) if(q<=1000) else print("{:.6f}".format(q*p*0.9))