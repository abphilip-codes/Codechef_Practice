# https://www.codechef.com/problems/BRACKETS

for _ in range(int(input())):
    s,b,m=input(),0,0
    for z in range(len(s)-1):
        if(s[z]=='('): b+=1
        else: b-=1
        m=max(b,m)
    for z in range(m): print("(",end='')
    for z in range(m): print(")",end='')
    print()