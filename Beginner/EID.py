# https://www.codechef.com/problems/EID

for T in range(int(input())):
    n,l,m=int(input()),sorted(list(map(int,input().split()))),9999999
    for z in range(len(l)-1):
        if(m>l[z+1]-l[z]): m=l[z+1]-l[z]
    print(m)