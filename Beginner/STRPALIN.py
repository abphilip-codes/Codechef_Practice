# https://www.codechef.com/problems/STRPALIN

for T in range(int(input())):
    a,b,s,k=input(),input(),"",0
    for i in range(len(a)):
        for j in range(len(b)):
            s=a[:i+1]+b[:j+1]
            if(s==s[::-1]): k=1
    print("Yes") if(k==1) else print("No")