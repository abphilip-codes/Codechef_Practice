# https://www.codechef.com/problems/TICKETS5

for T in range(int(input())):
    s,k=input(),0
    if(s[0]==s[1]): k=1
    for i in range(len(s)):
        if((i%2!=0 and s[i]==s[1]) or (i%2==0 and s[i]==s[0])): continue
        else: k=1
    print("YES") if(k==0) else print("NO")