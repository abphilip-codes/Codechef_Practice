# https://www.codechef.com/problems/COPS

for T in range(int(input())):
    M,x,y=map(int,input().split())
    m,a = list(map(int,input().split())),list(range(1,101))
    for i in m:
        for j in range(i-x*y,i+1+x*y):
            if(j in a): a.remove(j)
    print(len(a))