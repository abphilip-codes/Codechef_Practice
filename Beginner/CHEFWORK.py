# https://www.codechef.com/problems/CHEFWORK

n,c,t=int(input()),list(map(int,input().split())),list(map(int,input().split()))
a,b = [x for y,x in sorted(zip(t,c))],[y for y,x in sorted(zip(t,c))]
if(1 in b and 2 in b and 3 in b): print(min(a[b.index(1)]+a[b.index(2)],a[b.index(3)]))
else: print(a[b.index(1)]+a[b.index(2)]) if(3 not in b) else print(a[b.index(3)])