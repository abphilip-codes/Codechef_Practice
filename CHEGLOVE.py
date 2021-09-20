# https://www.codechef.com/problems/CHEGLOVE

for T in range(int(input())):
    n,l,g1=int(input()),list(map(int,input().split())),list(map(int,input().split()))
    g2,check1,check2=g1[::-1],0,0
    for z in range(n):
        if(l[z]>g1[z]): check1=1
        if(l[z]>g2[z]): check2=1
    if(check1==1 and check2==1): print("none")
    elif(check1==1): print("back")
    elif(check2==1): print("front")
    else: print("both")