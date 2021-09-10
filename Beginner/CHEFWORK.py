# https://www.codechef.com/problems/CHEFWORK

n,c,t=int(input()),list(map(int,input().split())),list(map(int,input().split()))
a,b = [x for y,x in sorted(zip(t,c))],[y for y,x in sorted(zip(t,c))]
print(min(a[b.index(1)]+a[b.index(2)],a[b.index(3)]))