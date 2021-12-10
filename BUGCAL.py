# https://www.codechef.com/problems/BUGCAL

for T in range(int(input())):
    l=list(map(int,input().split()))
    a,b,s=str(max(l)),"0"*(len(str(max(l)))-len(str(min(l))))+str(min(l)),0
    for z in range(len(a)): s = s*10 + (int(a[z])+int(b[z]))%10
    print(s)