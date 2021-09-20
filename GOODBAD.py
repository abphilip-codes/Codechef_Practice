# https://www.codechef.com/problems/GOODBAD

for T in range(int(input())):
    l,k=map(int,input().split())
    s,c,b=input(),0,0
    for i in s:
        if(i>='A' and i<='Z'): c+=1 
        if(i>='a' and i<='z'): b+=1 
    if(c<=k and b<=k): print("both")
    elif(c<=k): print("chef")
    elif(b<=k): print("brother")
    else: print("none")