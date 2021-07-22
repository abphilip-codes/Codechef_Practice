# https://www.codechef.com/problems/CHEFSTLT

for T in range(int(input())):
    s1,s2,m,n = input(),input(),0,0
    for z in range(len(s1)):
        if(s1[z]=='?' or s2[z]=='?'): m,n=m,n+1 
        elif(s1[z]!=s2[z]): m,n=m+1,n+1 
    print(m,n)