# https://www.codechef.com/problems/SIMPSTAT

for T in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    print("{:.6f}".format(sum(l[k:n-k])/len(l[k:n-k])))