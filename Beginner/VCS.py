# https://www.codechef.com/problems/VCS

for T in range(int(input())):
    N,M,K=map(int,input().split())
    n,m,k=set(list(range(1,N+1))),set(list(map(int,input().split()))),set(list(map(int,input().split())))
    print("{} {}".format(len(m&k),len(n-(m|k))))