# https://www.codechef.com/problems/COOMILK

for T in range(int(input())):
    n,l,k=int(input()),list(map(str,input().split())),1
    for z in range(n-1):
        if(l[z]=="cookie" and l[z+1]!="milk"): k=0
    if(l[n-1]=="cookie"): k=0
    print("NO") if(k==0) else print("YES")