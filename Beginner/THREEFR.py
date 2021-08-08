# https://www.codechef.com/problems/THREEFR

for T in range(int(input())):
    n=sorted(list(map(int,input().split())))
    print("yes") if(n[2]==sum(n[0:2])) else print("no")