# https://www.codechef.com/problems/ADACRA

for T in range(int(input())):
    s,u,d=input(),0,0
    if(s[0]=='U'): u+=1
    elif(s[0]=='D'): d+=1
    for z in range(1,len(s)):
        if(s[z]=='D' and s[z-1]=='U'): d+=1
        elif(s[z]=='U' and s[z-1]=='D'): u+=1
    print(min(d,u))