# https://www.codechef.com/problems/CATSDOGS

for T in range(int(input())):
    c,d,l=map(int,input().split())
    print("yes") if(l in range(d*4+(max(0,(c-d*2)))*4,d*4+c*4+1)) else print("no")