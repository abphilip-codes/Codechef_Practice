# https://www.codechef.com/problems/EXAM1

for T in range(int(input())):
    n,s,u,ans,z=int(input()),input(),input(),0,0
    while(z<n):
        if(s[z]==u[z]): ans+=1 
        elif(u[z]!='N'): z+=1
        z+=1
    print(ans)