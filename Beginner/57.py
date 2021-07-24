# https://www.codechef.com/problems/TWOSTR

for T in range(int(input())):
    a,b,s=input(),input(),0
    for i in range(len(a)):
        if(a[i]==b[i] or a[i]=="?" or b[i]=="?"): s+=1 
    print("Yes") if(s==len(a)) else print("No")