# https://www.codechef.com/problems/JDELAY

for T in range(int(input())):
    c=0
    for n in range(int(input())):
        a,b=map(int,input().split())
        if(abs(a-b)>5): c+=1 
    print(c)