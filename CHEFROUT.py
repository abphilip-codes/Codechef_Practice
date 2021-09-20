# https://www.codechef.com/problems/CHEFROUT

for T in range(int(input())):
    l,s,v=['C','E','S'],input(),0
    for z in range(len(s)):
        if(l.index(s[z])>v): v=l.index(s[z])
        elif(l.index(s[z])==v): continue
        else: 
            print("no")
            break
    else: print("yes")