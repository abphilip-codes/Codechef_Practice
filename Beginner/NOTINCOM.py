# https://www.codechef.com/problems/NOTINCOM

for T in range(int(input())):
    n,m=map(int,input().split())
    a,b=list(map(int,input().split())),list(map(int,input().split()))
    print(len(set(a))+len(set(b))-len(set(a+b)))