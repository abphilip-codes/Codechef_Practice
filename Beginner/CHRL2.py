# https://www.codechef.com/problems/CHRL2

s,ans=input(),0
for z in range(len(s)):
    if(s[z]=='C' and s[z-1]!='C'): ans+=1 
print(ans)