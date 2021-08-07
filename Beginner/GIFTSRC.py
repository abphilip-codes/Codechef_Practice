# https://www.codechef.com/problems/GIFTSRC

for T in range(int(input())):
    n,s=int(input()),input()
    x=y=0
    for i in range(n):
        if(i!=0): 
            if(s[i] in ['L','R'] and s[i-1] in ['L','R']): continue
            if(s[i] in ['U','D'] and s[i-1] in ['U','D']): continue
        if(s[i]=='L'): x-=1 
        if(s[i]=='R'): x+=1 
        if(s[i]=='U'): y+=1 
        if(s[i]=='D'): y-=1 
    print("{} {}".format(x,y))