# https://www.codechef.com/problems/CHRL2

s,l=input(),[0]*4
for z in range(0,len(s)):
    if(s[z]=='C'): l[0]+=1 
    elif(s[z]=='H'): 
        if(l[0]>0): l[0],l[1]=l[0]-1,l[1]+1
    elif(s[z]=='E'): 
        if(l[1]>0): l[1],l[2]=l[1]-1,l[2]+1
    elif(s[z]=='F'): 
        if(l[2]>0): l[2],l[3]=l[2]-1,l[3]+1
print(l[-1])