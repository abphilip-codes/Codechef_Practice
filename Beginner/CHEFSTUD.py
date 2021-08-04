# https://www.codechef.com/problems/CHEFSTUD

for T in range(int(input())):
    s1,s2,s3=input(),'',0
    for a in range(len(s1)): 
        if(s1[a]=='>'): s2+='<'
        elif(s1[a]=='<'): s2+='>'
        else: s2+=s1[a]
    for a in range(len(s1)-1):
        if(s2[a]=='>' and s2[a+1]=='<'): s3+=1
    print(s3)