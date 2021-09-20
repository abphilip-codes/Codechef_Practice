# https://www.codechef.com/problems/ATTND

for T in range(int(input())):
    n,f,l=int(input()),[],[]
    for i in range(n):
        lf,ll=input().split(" ")
        f.append(lf)
        l.append(ll)
    for i in range(n):
        print(f[i]+" "+l[i]) if(f.count(f[i])!=1) else print(f[i])