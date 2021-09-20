# https://www.codechef.com/problems/FANCY

for T in range(int(input())):
    s=input()
    for z in range(len(s)):
        if(s[z]=='n' and z in range(0,len(s)-2)):
            if(s[z+1]=='o' and s[z+2]=='t'):
                if((z+3==len(s) or s[z+3]==' ') and (z==0 or s[z-1]==' ')):
                    print("Real Fancy")
                    break
    else: print("regularly fancy")