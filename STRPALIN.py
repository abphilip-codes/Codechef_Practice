# https://www.codechef.com/problems/STRPALIN

for T in range(int(input())):
    a,b,k=input(),input(),0
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if(a[i]==b[j]): 
                k=1
                print("Yes")
                break
        if(k==1): break
    else: print("No")