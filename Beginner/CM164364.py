# https://www.codechef.com/problems/CM164364

for _ in range(int(input())):
    n,x=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    print(min(n-x,len(set(a)))) 