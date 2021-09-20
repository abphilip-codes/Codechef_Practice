# https://www.codechef.com/problems/XYSTR

for T in range(int(input())):
    s,ans,z=input(),0,0
    while(z<len(s)-1):
        if(abs(ord(s[z])-ord(s[z+1]))==1): ans,z=ans+1,z+1
        z+=1
    print(ans)