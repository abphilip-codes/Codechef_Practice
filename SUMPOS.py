# https://www.codechef.com/problems/SUMPOS

for T in range(int(input())):
    l=sorted(list(map(int,input().split())))
    print("NO") if(l[2]!=l[1]+l[0]) else print("YES")