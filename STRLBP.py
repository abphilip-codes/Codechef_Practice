# https://www.codechef.com/problems/STRLBP

for T in range(int(input())):
    s,c=input(),0
    s+=s[0]
    for i in range(8):
        if(s[i]!=s[i+1]): c+=1 
    print("uniform") if(c<=2) else print("non-uniform")