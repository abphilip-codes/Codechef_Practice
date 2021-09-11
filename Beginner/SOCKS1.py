# https://www.codechef.com/problems/SOCKS1

l=list(map(int,input().split()))
for z in range(1,11): 
    if(l.count(z)>=2):
        print("YES")
        break
else: print("NO")